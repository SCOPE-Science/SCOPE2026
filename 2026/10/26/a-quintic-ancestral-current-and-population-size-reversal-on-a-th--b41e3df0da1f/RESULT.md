# Exact ancestral current and global direction on a symmetric three-site killing line

## Finding

On the complete three-site graph with unit motion rates and three uniformly copying Fleming–Viot particles, set the killing rates to \(k=(1-\varepsilon,1,1+\varepsilon)\), with \(-1<\varepsilon<1\). The ancestral port current from site \(0\) toward site \(2\), net of the reverse port, is

\[
\Delta_3(\varepsilon)=\frac{24\varepsilon^5(16-3\varepsilon^2)(38448+479\varepsilon^2)}{(790272+4704\varepsilon^2+279\varepsilon^4+5\varepsilon^6)(11757312-137808\varepsilon^2+840\varepsilon^4+143\varepsilon^6)}.
\]

In particular \(\operatorname{sgn}\Delta_3(\varepsilon)=\operatorname{sgn}\varepsilon\) throughout the admissible interval: the small-contrast current direction persists at all positive contrasts, and equal killing is the only zero. The previously reported local expansion \(89\varepsilon^5/56010528+O(\varepsilon^7)\) [2] is recovered. The local difference from the larger-population cubic response [1,2] is context, not a new claim.

## Model and conventions

Each particle moves from its site to any other at rate one per destination. On killing at site \(i\) it is immediately replaced at the site of a uniformly drawn distinct donor and inherits the donor's label. Same-site copying can change labels. Write \(c\) for the three site counts and \(e_i\) for the site basis vectors. Write \(h(i,d)\) for the probability that a uniquely labelled founder at site \(i\) attains fixation, with counts \(d\) of the other two particles. If \(\pi\) denotes the stationary law of \(c\), the current convention of [1] is
\[
F_{ij}=\sum_{c:c_i>0}\pi(c)c_i h(j,c-e_i),\qquad \Delta_3=F_{02}-F_{20}.
\]

## Proof

The ten-state count generator has off-diagonals \(L(c,c-e_a+e_b)=c_a(1+c_b k_a/2)\) for distinct \(a,b\) with \(c_a>0\); its diagonal gives row sum zero. Motion ensures irreducibility. The stationary vector is the unique solution of \(\pi L=0\), \(\sum_c\pi(c)=1\).

For the eighteen founder states \((i,d)\), the harmonic equations are \(Th=0\), where
\[
\begin{aligned}
(Tg)(i,d)={}&\sum_{j\ne i}[g(j,d)-g(i,d)]
+\sum_a d_a\sum_{b\ne a}[g(i,d-e_a+e_b)-g(i,d)]-k_i g(i,d)\\
&+\sum_a d_a k_a\left[g(i,d-e_a+e_i)
+\frac12\sum_b(d_b-\mathbf1_{a=b})g(i,d-e_a+e_b)-g(i,d)\right].
\end{aligned}
\]
Omit terms with \(d_a=0\) or with zero donor multiplicity. The term \(-k_i g(i,d)\) accounts for founder death. An ordinary particle copying the founder produces two descendants at \(i\); giving them distinct temporary labels at the transition shows that subsequent combined fixation probability is the sum of their two identical one-founder probabilities. This factor of two cancels the probability \(1/2\) of drawing the founder. An ordinary particle's other donor has counts \(d_b-\mathbf1_{a=b}\) after excluding the killed particle. This accounts for same-site copying as well as spatial relocations.

The finite label process almost surely coalesces: from any state, a finite sequence of deaths and copies can propagate one chosen label to all three particles, with positive probability bounded below uniformly over the finite state space for fixed positive rates. The same sequence gives \(h>0\) in every founder state. Thus \(\operatorname{diag}(h)^{-1}T\operatorname{diag}(h)\) has nonnegative off-diagonals, row sums zero and an irreducible motion subgraph. Its kernel consists of constants. Even after dropping the founder equation at the anchor, the other rows imply the dropped row by the strictly positive stationary law of that transformed generator. Exchangeability at the anchor \(h(0,(2,0,0))=1/3\) now gives a nonsingular replaced-row system.

The accompanying `verify_fleming_viot.py` constructs both systems with entries affine in \(\varepsilon\), replaces a row in each by its normalization, and solves over \(\mathbb Q(\varepsilon)\) by exact Gaussian elimination. It computes \(\sum_{c:c_0>0} \pi(c)c_0h(2,c-e_0)-\sum_{c:c_2>0}\pi(c)c_2h(0,c-e_2)\) and cancels the difference from the factored expression under Finding to zero. The nonsingularity just proved makes the rational identity valid throughout the admissible real interval.

Put \(u=\varepsilon^2<1\). The first denominator factor is positive term by term, with positive constant. The second is at least \(11757312-137808>0\). Both \(16-3u\) and \(38448+479u\) are positive. Consequently the sign is exactly that of \(\varepsilon^5\), including zero. Analyticity of the factors in \(u\) gives the cited expansion with leading constant \(24\cdot16\cdot38448/(790272\cdot11757312)=89/56010528\).

## Verification

Run `python verify_fleming_viot.py` with Python and SymPy. The rational identity check is exact, rather than a test at finitely many fixed contrasts. The script also checks two contrasts by an alternative 36-transient-state two-colour absorption calculation and reproduces [1]'s exact example at \(k=(1,2,4)\); see `verification_output.txt` for the recorded execution. Those supplementary checks alone do not prove the all-contrast identity.

## Prior results and limitations

Lin and Lu [1] prove generic nonzero circulation for each \(N\ge3\), which does not exclude zero or sign changes along a specified line of killing vectors. Their three-particle calculation at \((1,2,4)\) is off the present line, and their cubic response for fixed \(N\ge4\) does not give its three-particle sign. The earlier finding [2] proves the fifth-order onset and local direction reversal on exactly this line, but expressly does not determine a global sign interval. The claim here is the global sign on the full positive-rate line and the explicit rational certificate for it. The theorem does not classify arbitrary positive killing triples, different motion graphs, or the all-contrast direction for larger populations. Unidentified prior all-contrast calculations are not ruled out.

## References

1. Y. Lin and T. Lu, *Ancestral circulation beyond two Fleming–Viot particles*, [arXiv:2610.12589v1](https://arxiv.org/html/2610.12589v1), Theorem 1.1, Eq. (1.10), Proposition 5.2 and the founder equations in Section 3.
2. *Fifth-order onset and sign reversal of three-particle ancestral circulation*, [Resultary, 2026-10-18](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-fifth-order-onset-and-sign-reversal-of-three-particle-ancestral--7e75e60ffd49/RESULT.md), Finding and Limitations.
