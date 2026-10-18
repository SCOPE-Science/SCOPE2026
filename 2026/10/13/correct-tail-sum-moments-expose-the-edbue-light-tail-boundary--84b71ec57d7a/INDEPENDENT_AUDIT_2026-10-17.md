# Independent mathematical audit

## correctness

PASS

From p_n=G_{n+1}-G_n, P(X>=k)=1-G_k~(alpha/lambda)theta^k/k with lambda=-log theta. Hence p_n~alpha(1-theta)/lambda *theta^n/n, PGF radius 1/theta, E(e^{tX}) finite precisely for t<lambda, and diverges harmonically at t=lambda. Tonelli on x^r=sum_{k<=x}(k^r-(k-1)^r) yields corrected moments sum_k (k^r-(k-1)^r)(1-G_k). The printed Eq6.4 summand ((k-1)^r-k^r)G_k~-r*k^(r-1), so its sum diverges to -infinity. Proof holds for all alpha>0,0<theta<1, integer r>=1.

## originality

PASS

Elementary survival tail-sum identities and MGF convergence criteria are prior, and even the source PMF asymptotic is known. The novel narrow result is a needed, explicitly corrected family-specific moment formula and rigorous identification of the source’s incorrect distribution interpretation; no exact prior corrigendum located.

## value

PASS

Provides convergent formulas for every population moment of a new actuarial/reliability family and resolves a substantive contradiction: the printed moment formula diverges and the claimed heavy-tail regimes cannot hold asymptotically. Despite relying on standard tail identities, source-specific validity matters for interpreting model shape and risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
