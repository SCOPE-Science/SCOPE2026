# The zero-, one-, and two-interior-point laws for random axial lattice triangles

## Finding
For integers \(a,b,c\ge1\), let \(T(a,b,c)\subset\mathbb R^3\) be the lattice triangle with vertices \((a,0,0)\), \((0,b,0)\), and \((0,0,c)\). Let \(I(a,b,c)\) count its *relative-interior* lattice points, equivalently the positive integer triples satisfying \(x/a+y/b+z/c=1\). Define the positive, absolutely convergent Euler products
\[
P=\prod_{p\text{ prime}}\left(1-\frac{3}{p^2}+\frac{2}{p^3}\right),\qquad
Q=\prod_{p\text{ prime}}\left(1-\frac{2}{p^2}+\frac{1}{p^3}\right).
\]
For \(j\in\{0,1,2\}\), the natural box density
\[
d_j=\lim_{X\to\infty}\frac{1}{\lfloor X\rfloor^3}\#\{1\le a,b,c\le\lfloor X\rfloor:I(a,b,c)=j\}
\]
exists and is exactly
\[
\boxed{d_0=3Q-\frac{15}{8}P,\qquad d_1=\frac{3583}{17280}P,\qquad d_2=\frac{151}{2100}P.}
\]
These are approximately \(0.7471\), \(0.0595\), and \(0.0206\), respectively (rounded, not rigorous decimal enclosures). In particular, each of the three small-interior strata has positive natural density.

## Assumptions and scope
Triples \((a,b,c)\) are **ordered** and uniformly averaged over integer cubes \([1,X]^3\). Lattice interior means the two-dimensional relative interior of the triangle in its affine plane; points on an edge are excluded. No generic-coprimality assumption is made. An exact finite-parameter classification underlies the densities: put
\[
g=\gcd(a,b,c),\qquad (u,v,w)=\operatorname{sort}\!\left(\frac{\gcd(a,b)}{g},\frac{\gcd(b,c)}{g},\frac{\gcd(c,a)}{g}\right).
\]
The three entries of \((u,v,w)\) are pairwise coprime and \(1\le u\le v\le w\). The complete list of configurations producing \(I\le2\) is:

| Interior count | All and only the patterns \((g;u,v,w)\) |
|---|---|
| \(0\) | \((1;1,1,w)\) for every \(w\ge1\); \((2;1,1,1)\) |
| \(1\) | \((3;1,1,1)\); \((2;1,1,2)\); \((1;1,2,3)\) |
| \(2\) | \((2;1,1,3)\); \((1;1,2,5)\) |

When unequal entries occur, every permutation of the three pair-GCD positions is allowed. The identities do not assert densities for any fixed larger interior count.

## Proof
**1. Lattice-Pick identity.** The normalized double area of the triangle, measured in its affine rank-two integer lattice, is \(D=\gcd(ab,ac,bc)\). Each edge has its usual lattice length \(\gcd(a,b)\), \(\gcd(b,c)\), or \(\gcd(c,a)\). Thus Pick's theorem (or Theorem A of Aldrich–Gulbrandsen–Keddy) gives
\[
I(a,b,c)=\frac{\gcd(ab,ac,bc)-\gcd(a,b)-\gcd(b,c)-\gcd(c,a)+2}{2}.
\]
At each prime, the smallest of the three valuations of \(a,b,c\) occurs in two of the three pairwise minima; consequently the three pairwise GCDs divided by \(g\) are pairwise coprime. Valuation by valuation, \(\gcd(ab,ac,bc)=\gcd(a,b)\gcd(b,c)\gcd(c,a)/g=g^2uvw\). Therefore
\[
2I=g^2uvw-g(u+v+w)+2. \tag{1}
\]
**2. Complete small-interior classification.** For \(g=1\), if \(u=v=1\), (1) yields \(I=0\), regardless of \(w\). If \(u=1\), \(v=2\), pairwise coprimality requires odd \(w\ge3\), and (1) reduces to \(I=(w-1)/2\), giving precisely \(w=3,5\) for \(I=1,2\). If \(u=1\), \(v\ge3\), then \(w\ge v+1\) and \(2I=(v-1)w-v+1\ge6\). If \(u\ge2\), pairwise coprimality and ordering force \(v\ge3\), \(w\ge5\), and the right side of (1) is at least \(22\). (The expression is strictly increasing in each variable on this region.)

For \(g\ge2\), if \(u=v=1\), (1) reads \(2I=g((g-1)w-2)+2\). The cases with \(I\le2\) are \(g=2\), \(w\in\{1,2,3\}\) and \(g=3\), \(w=1\), giving the listed patterns. For \(u=1\), \(v\ge2\), the minimum is \((g,u,v,w)=(2,1,2,3)\), with \(I=7\); for \(u\ge2\), the count is larger. This proves the complete table.

**3. Local densities.** For a random integer triple, the probability that at most one coordinate is divisible by a fixed prime \(p\) is \(e_p=1-3/p^2+2/p^3\), so the limiting pairwise-coprime density is \(P=\prod e_p\). The probability that a *specified* coordinate is coprime to both others is \(Q=\prod h_p\), where \(h_p=1-2/p^2+1/p^3\). The intersection of any two of these three events is the all-pairs-coprime event; inclusion-exclusion gives \(3Q-2P\). The remaining \(I=0\) pattern \((2;1,1,1)\) has density \(P/8\) (factor \(2^3\) out of the variables and require pairwise coprimality), proving \(d_0=3Q-15P/8\).

For an exact *specified* pair GCD equal to a prime \(p\), with all other pair GCDs equal to one, the local relative factor compared with pairwise coprimality is
\[
r_p=\frac{(1-p^{-1})(p^{-2}-p^{-4})}{e_p}=\frac{p+1}{p^2(p+2)}.
\]
In particular \(r_2=3/16\), \(r_3=4/45\), and \(r_5=6/175\). Requiring \(p\) to divide all three coordinates once, after which the divided triple is pairwise coprime, contributes relative factor \(p^{-3}\). The pattern with pair GCDs \((2,2,4)\) contributes relative factor \(3/128\) per choice of strong pair: at \(p=2\), the two strongly divisible coordinates have minimum valuation exactly two and the remaining coordinate valuation exactly one; its local probability is \((2^{-1}-2^{-2})(2^{-4}-2^{-6})=3/256\), to be divided by \(e_2=1/2\).

The three \(I=1\) types have densities, respectively,
\[
\frac{P}{27},\qquad 3\frac{3P}{128}=\frac{9P}{128},\qquad 6r_2r_3P=\frac P{10}.
\]
Their sum is \((3583/17280)P\). The two \(I=2\) types have densities, respectively,
\[
3\frac18r_3P=\frac P{30},\qquad 6r_2r_5P=\frac{27P}{700}.
\]
Their sum is \((151/2100)P\). These events are disjoint by the exact classification.

**4. Passage from finite primes to natural densities.** For every fixed finite set of primes and specified finite valuation conditions, the Chinese remainder theorem gives exactly the product of the local probabilities in the box limit. For the unrestricted products, the probability that some prime \(p>Y\) divides two of the three coordinates is at most \(3\sum_{p>Y}p^{-2}\le3/Y\), uniformly in the box size (since \(\Pr(p\mid a)\le1/p\)). The prescribed exceptional prime powers occur only at \(2,3,5\), so the same tail estimate applies to the remaining baseline-pairwise-coprimality constraints. Taking box size to infinity and then \(Y\to\infty\) proves the displayed limits. The factors are \(1+O(p^{-2})\) and positive, proving absolute Euler-product convergence and positivity.

## Verification
The standalone `verify.py` uses only Python's standard library. It checks (1), compares the classification to **independently enumerated positive integer solutions** of \(x/a+y/b+z/c=1\) for every ordered triple with \(1\le a,b,c\le25\), verifies the rational local factors, and checks the two rational-coefficient identities. Run `python3 verify.py`; the expected final line is `VERIFY_OK`. These finite checks are auxiliary; the unrestricted density statement follows from the preceding proof and CRT/tail argument, not computation.

## Relationship to prior work
Aldrich, Gulbrandsen, and Keddy (2026, Theorem A, Section 3.1, arXiv:2610.20899v1) establish the pointwise normalized-area/GCD formula for the same axial triangles; they do **not** derive the three box-density laws or the small-interior gcd-pattern classification. Heyman (2013, arXiv:1309.5578, Introduction and Section 4) computes the density of pairwise non-coprime integer triples using inclusion-exclusion and the product \(Q\). Together with elementary GCD data, this substantially anticipates the \(I=0\) density component, and no separate novelty is claimed for the underlying coprimality constants. The one- and two-interior strata require additional prime-adic valuation strata, local ratios, and complete classifications; these do not follow as stated from either inspected source. Both papers were inspected in accessible full-text HTML, not merely from search snippets.

## Limitations
No explicit asymptotic error term is proved. Neither the exact distribution for \(I\ge3\) nor density laws under non-box sampling are treated. The computation confirms finitely many triples, not asymptotics. The originality comparison is not exhaustive of unpublished computations, theses, and unindexed lattice-triangle density tables; in particular the zero-interior constant is closely related to existing coprimality asymptotics.

## References
1. Max Aldrich, Daniel Gulbrandsen, Clara Keddy, *Ehrhart Polynomials of Triangles in R³*, arXiv:2610.20899v1, first posted 14 October 2026. https://arxiv.org/html/2610.20899v1
2. Randell Heyman, *Pairwise non-coprimality of triples*, arXiv:1309.5578, 2013. https://arxiv.org/abs/1309.5578
3. Classical Pick theorem and the Chinese remainder theorem, used in their standard forms.
