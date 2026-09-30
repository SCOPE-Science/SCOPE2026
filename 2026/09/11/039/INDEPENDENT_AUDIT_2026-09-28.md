# Independent audit — 2026-09-28

Record: `2026/09/11/039`  
Audited tree: `ad67c859dd48abaa759d570c7484f8c63a23ae52`  
Disposition: **passed**

## Correctness

Independent matrix arithmetic with `sigma1 -> [[1,1],[0,1]]` and `sigma2 -> [[1,0],[-1,1]]` gives `Delta^2 -> -I`, `gamma=sigma1 sigma2^-1 -> [[2,1],[1,1]]` with trace 3, and `beta*=gamma Delta^2 -> -gamma` with trace -3. Hence the projective class and stretch factor are unchanged and equal `(3+sqrt(5))/2`. Exponent sum is 0 for every power of gamma and 6 for beta*, so conjugacy to any gamma power is excluded. The displayed word has seven alternating syllables. The quartic `t^4-3t^3-t^2+3t-1` has its largest real root about 3.0399166, so the target's quoted 2.747 floor value was numerically inconsistent as stated.

## Originality

The counterexample is target-specific rather than a new structural theorem. Standard braid references already make the center quotient explicit, and published work notes that multiplying a pseudo-Anosov braid by a full twist preserves its mapping-class image/pseudo-Anosov type. Thus the novelty is the diagnosis of this particular proposed floor and the explicit witness, not central-twist invariance itself.

## Scientific value

That diagnosis is still useful: it prevents a false isolation statement from being propagated and identifies the missing hypothesis (control of center power or another invariant). The package is appropriately a negative result.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/039 ; https://arxiv.org/abs/1004.5344 ; https://ambp.centre-mersenne.org/item/10.5802/ambp.293.pdf ; https://nyjm.albany.edu/j/2020/26-26v.pdf
