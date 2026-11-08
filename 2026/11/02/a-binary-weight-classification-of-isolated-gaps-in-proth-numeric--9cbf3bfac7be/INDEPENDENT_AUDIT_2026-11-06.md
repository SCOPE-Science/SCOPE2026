# Independent mathematical audit

## correctness

PASS

The final universal claim is for all m>=3 in S_m=<2^i(m-1)+1> and Proth m=k2^n+1 with n>=3, odd 1<=k<2^n. For each nonzero residue r the Apéry minimum w_r=(m-1)(m-r)+mL(m-r) follows from the generator identity and the larger-t cutoff. L(t+1)-L(t)=+/-1: append one 1-coin, and from an optimal t+1 representation delete a 1 or replace 2^i-1 by two copies of 2^(i-1)-1. All nonresidue-one gaps have a preceding gap, and the residue-one successor test equals m(1+L(m-1)-L(m-2)), either 0 or 2m. Thus zero or exactly two isolated gaps. In the latter case the final step f(m-1)-f(m-2)=2m-1 dominates possible earlier one-step declines, making w1 maximal and F=w1-m; isolated gaps are F-m,F. Binary splitting and absence of carries for j<2^(n-1) yield the criterion s2(k) in {2j+1-s2(j):j>=0}. No empty-case Frobenius formula is asserted. Independent integer Dijkstra/coin dynamic program verified m=3..71 and exact isolated-gap lists, not an infinite proof. Previously supplied verify.py inspection confirms wider explicit ranges; its output is not adopted as an external proof.

## originality

PASS

Best-of-knowledge O PASS for the precise assessed final statement. Reviewed the actual final package and compared statements/implications with primary literature and published SCOPE/Resultary semantic results, using aliases, broader cases, tables and corollary checks. A binary-weight classification of isolated gaps in Proth numerical semigroups: the cited prior results cover background tools, objects and/or weaker observables; no identified theorem implies the complete evaluated final statement. Negative search is not a novelty proof; primary-source limitations and risks are explicit.

## value

PASS

A motivated natural family of numerical semigroups already studied for Frobenius and Apéry data: whether it is perfect (no isolated gaps) is a discrete structural property, and the zero-or-two rigidity plus digit-weight-only classification across all n and k is nontrivial, usable for gap-theoretic classification. This is not an arbitrary small-parameter census or a generic algorithm merely rerun.

The dated certificate retains the supplied scientific assessment, sources and limitations.
