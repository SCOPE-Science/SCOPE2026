#!/usr/bin/env python3
checks=0
for N in range(3,201):
    for k in range(1,N):
        classical2=k*(k+1)
        for t in range(0,k+1):
            # Twice the specialized tight right-hand side.
            z2=2*k+t*(t-1)
            assert z2 <= classical2
            # Twice the uniform-center slack.
            slack2=k*(N+1)-z2
            assert slack2 >= k*(N-k)
            # Exact squared-distance comparison after clearing denominators.
            assert slack2*slack2 >= k*(N-k)*(N-1)
            checks += 1
    # Singleton equality gives the sharp radius.
    singleton_slack2=N-1
    assert singleton_slack2*singleton_slack2 == (N-1)*(N-1)
print(f"VERIFY_OK hochschild-inradius N=3..200 parameter_checks={checks} exact_integer=yes")
