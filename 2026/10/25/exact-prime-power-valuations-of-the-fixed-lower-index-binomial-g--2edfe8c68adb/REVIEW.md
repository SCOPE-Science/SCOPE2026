# Independent mathematical audit

## correctness

PASS

Reconstructed dependence on published Guo–Qiu–Cao–Feng–Gao Lemmas 4 and 9 (no p outside n; support iff m<=p^a). For p^a||n, m=n/p^a, L=floor(log_p m), if L>=a then m>p^a (since p∤m), support lemma yields exponent zero. Else for any q, b=v_p(q-1), carries at b<j<=a and at a+L<j<=a+b yield min exponent >=max(0,a-b)+max(0,b-L)>=a-L. For m=1, q=2 attains a; for 2<=m<p^a the permitted q=1+t p^a has digit-block identity v_p binom(qk,k)=a-v_p binom(m-1,t), and t=p^L-1 (or t=1 when L=0) attains a-L by Kummer. Checked endpoints and witness q<=n. Fresh independent direct p-factorial valuation minima for 789 pairs (n<=400), direct integer gcd n3..35, all agree.

## originality

PASS

Guo et al. 2026 solve the support/gcd-one criterion and provide relevant lemmas, but positive valuations are not specified by that Boolean statement. The target formula uniquely determines all prime-power components and explicit witness multipliers; classic row-gcd families have different varying indices.

## value

PASS

The full value, not mere support, of the natural binomial gcd underlying the recent criterion is a complete exact invariant with nontrivial p-adic carry optimization and witness selection. It yields D(k)|k+1 and precise prime-power cases; unlike a routine relabeling of a Boolean theorem, it resolves extra numerical multiplicity data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
