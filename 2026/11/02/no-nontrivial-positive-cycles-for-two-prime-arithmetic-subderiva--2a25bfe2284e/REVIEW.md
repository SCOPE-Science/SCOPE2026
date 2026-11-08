# Independent mathematical audit

## correctness

PASS

For arbitrary distinct primes p,q and positive integer n, every positive periodic orbit of D(n)=n(ν_p(n)/p+ν_q(n)/q) has positive multipliers U_i=qν_p(n_i)+pν_q(n_i) whose cyclic product is (pq)^L. Thus each U_i is p,q-smooth and satisfies U_next=U-(p+q)+qν_p(U)+pν_q(U). If U>pq and smooth, the three cases U=p^a q^b with both a,b>=1, only p power, or only q power all force U_next>pq. If any cyclic U_i were above pq all would be above, contradicting product (pq)^L. All U_i<=pq with product equality forces U_i=pq and every orbit term is fixed. The Diophantine equation qa+pb=pq yields only (a,b)=(p,0) or (0,q), so fixed n=p^p m or q^q m with gcd(m,pq)=1. Independently checked the prime-smooth threshold on 1227 cases for 21 prime pairs; finite check corroborates but is not the arbitrary-prime proof. Checked source proof and standard-library diagnostic script.

## originality

PASS

The closest published Resultary finding proves no positive nontrivial cycles only for {2,3}; its full RESULT.md was read, and its proof explicitly says it does not immediately extend to arbitrary distinct primes. The present theorem strictly subsumes it via a uniform p,q-smooth invariant-threshold proof. Talukdar–Saikia studies arithmetic subderivative fixed points for general finite prime sets, which is not the assertion that no higher cycles occur. Best of knowledge the universal two-prime aperiodicity is additional.

## value

PASS

The natural dynamical question for arithmetic subderivatives is whether nontrivial positive periodic orbits exist. This infinite sharp classification for *all* two-prime supports resolves a materially broader case than the known {2,3} result and explains the rigidity by an invariant multiplicative threshold; useful before attacking three or more prime supports.

The dated certificate retains the supplied scientific assessment, sources and limitations.
