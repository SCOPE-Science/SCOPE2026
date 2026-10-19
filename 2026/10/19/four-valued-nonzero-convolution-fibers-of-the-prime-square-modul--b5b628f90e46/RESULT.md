# Four-valued nonzero convolution fibers of the prime-square modular hyperbola

## Finding

Let \(p\ge5\) be prime, \(R=\mathbb Z/p^2\mathbb Z\), \(U=R^\times\), and
\[C=\{(u,u^{-1}):u\in U\}\subset R^2.\]
For \((s,y)\in R^2\), let \(r(s,y)\) be the number of **ordered** pairs \((u,v)\in U^2\) with
\[u+v=s,\qquad u^{-1}+v^{-1}=y.\]
The complete multiplicity distribution (including zero fibers) is

| \(r(s,y)\) | Number of targets \((s,y)\) |
|---:|---:|
| \(0\) | \(p^4-1-p(p-1)-(p-1)^2/2-p^2(p-1)(p-3)/2\) |
| \(2\) | \(p^2(p-1)(p-3)/2\) |
| \(p\) | \(p(p-1)\) |
| \(2p\) | \((p-1)^2/2\) |
| \(p(p-1)\) | \(1\) |

In particular, the additive energy (equivalently the squared \(\ell^2\)-norm of the convolution) is
\[E(C):=\sum_{(s,y)\in R^2}r(s,y)^2=3p^2(p-1)(2p-3),\]
and the geometric Minkowski sum has size
\[|C+C|=1+p(p-1)+\frac{(p-1)^2}{2}+\frac{p^2(p-1)(p-3)}{2}.\]
Writing the **unnormalized** complete Kloosterman sums as
\[K_p(a,b)=\sum_{u\in U}\exp\!\left(\frac{2\pi i(au+bu^{-1})}{p^2}\right),\]
normalized orthogonality on the full frequency group gives
\[\frac1{p^4}\sum_{a,b\in R}|K_p(a,b)|^4=E(C),\qquad\frac{E(C)}{|C|^2}=6-\frac3{p-1}.\]
The last quantity is the constant-coefficient fourth-power Fourier-extension quotient; it is **not** asserted to be the sharp operator norm over arbitrary coefficient functions.

## Assumptions and scope

All sums/products/congruences defining \(C\) and \(r\) are in \(R\). Ordered representations count \((u,v)\) separately from \((v,u)\) when unequal. Divisibility by \(p\) means reduction to zero in \(\mathbb F_p\). Only primes \(p\ge5\) are asserted, ensuring the four positive fiber levels \(2,p,2p,p(p-1)\) are pairwise distinct. The frequency average includes **all** \(p^4\) pairs in \(R^2\), not just pairs of units.

## Proof

**Step 1: valuation constraint and quadratic reduction.** For unit \(u,v\), their product is a unit, and
\[u^{-1}+v^{-1}=\frac{u+v}{uv}.\]
Thus \(s\) and \(y\) have the same \(p\)-adic valuation in \(\{0,1,2\}\), where valuation \(2\) denotes zero modulo \(p^2\). These are the only possible support strata.

**Step 2: both coordinates units.** Fix \(s\in U\). The product \(t=sy^{-1}\in U\) is determined by \(y\in U\), and a representation is equivalent to a root \(u\in R\) of
\[u^2-su+t=0,\qquad v=s-u.\]
A root and its companion are automatically units because their product \(t\) is a unit. Since \(2\) is invertible, putting \(z=2u-s\) gives the bijective condition
\[z^2=\Delta,\qquad \Delta=s^2-4t.\]
As \(y\) runs over \(U\), \(t\) runs bijectively over \(U\), and hence \(\Delta\) runs over precisely the residues satisfying \(\Delta\not\equiv s^2\pmod p\). For a nonzero square \(\Delta\bmod p\), Hensel lifting gives exactly two roots \(z\bmod p^2\); for \(\Delta=0\bmod p^2\), exactly the \(p\) residues divisible by \(p\) are roots; and for \(\Delta\equiv0\bmod p\) but \(\Delta\ne0\bmod p^2\), there is no root. There are \((p-3)/2\) admissible nonzero square classes \(\Delta\bmod p\), because the class \(s^2\) is excluded. Each class has \(p\) lifts. Hence each fixed unit \(s\) has \(p(p-3)/2\) targets with \(r=2\), and one target \(\Delta=0\) with \(r=p\). Multiplying by \(|U|=p(p-1)\) gives the first two positive counts.

**Step 3: both coordinates have valuation one.** Write \(s=p\alpha\), \(y=p\beta\), where \(\alpha,\beta\in\mathbb F_p^\times\). Reduction of \(u+v=s\) yields \(\bar v=-\bar u\). The relation \(yuv=s\) reduces, after division by \(p\), to
\[-\beta\bar u^2=\alpha\quad\text{in }\mathbb F_p.\]
There are two nonzero choices of \(\bar u\) precisely when \(-\alpha/\beta\) is a square, and no choices otherwise. Each allowed \(\bar u\) has \(p\) lifts \(u\in U\), with the companion \(v=s-u\) uniquely determined and a unit. Therefore \(r(s,y)=2p\) exactly on \((p-1)^2/2\) valuation-one targets and vanishes on the others.

**Step 4: zero and exhaustion.** For \((s,y)=(0,0)\), every \(u\in U\) gives \(v=-u\), so \(r(0,0)=p(p-1)\). No mixed-valuation target is representable by Step 1. Together Steps 2--4 exhaust all \(p^4\) targets and give the entire table, including its zero row.

**Step 5: energy and Fourier moment.** Squaring each positive multiplicity and summing produces
\[\begin{aligned}E(C)&=4\frac{p^2(p-1)(p-3)}2+p^2p(p-1)+(2p)^2\frac{(p-1)^2}{2}+p^2(p-1)^2\\&=3p^2(p-1)(2p-3).\end{aligned}\]
For a finite abelian group, character orthogonality identifies the average fourth power of the Fourier transform of \(1_C\) with the number of ordered solutions \(c_1+c_2=c_3+c_4\) in \(C\), namely \(E(C)\). This proves the stated normalization exactly.

## Verification

`verify.py` exhaustively forms the ordered convolution for primes \(5,7,11,13,19\), compares every fiber level and multiplicity with the formulas, checks total representation counts \(\sum r=|U|^2\), checks \(|C+C|\), and checks the additive-energy formula. Run `python3 verify.py` from the extracted package directory. The expected deterministic output is included as `verification_output.txt`; these small-modulus checks are corroboration, not the proof of all primes.

## Relationship to prior work

Hickman and Wright (arXiv:1801.03176, first public 2018-01-09, MSC 42B10) develop Fourier restriction over \(\mathbb Z/N\mathbb Z\), primarily treating paraboloids and scale-dependent estimates; the present exact inverse-curve constant-input moment and full convolution fibers are different quantitative data. Humphries (arXiv:2003.09955) studies distribution, discrepancy and mixing for the same inverse-point set as \(N\) varies, without an exact prime-square Minkowski two-sum spectrum. Ricotta and Royer (2018, Proposition 5.4 and Section 5.2) use the same sum-and-reciprocal-sum collision congruences for *upper bounds* on incomplete Kloosterman fourth moments; the exact four-stratum prime-square fiber table is stronger data than such an aggregate bound. Bower, Evans, Luo and Miller (arXiv:1212.2930, Theorem 3.6) classify *coordinate sums within one hyperbola point* \(u+u^{-1}\), not pairwise vector sums \((u,u^{-1})+(v,v^{-1})\). Published finite-field hyperbola Fourier-extension results concern fields of cardinality \(q\), not the ring \(\mathbb Z/p^2\mathbb Z\). These comparisons do not constitute a proof that no equivalent result appears elsewhere.

## Limitations

The theorem is for odd prime-square moduli with \(p\ge5\), not general prime powers or composite moduli. It concerns the **constant-input** fourth moment, not an unrestricted sharp restriction constant, and does not classify weighted-input extremizers. Elementary modular-quadratic identities underpin the classification, so an undiscovered earlier complete evaluation or implicit derivation in Kloosterman literature is a genuine originality risk.

## References

1. J. Hickman and J. Wright, *The Fourier Restriction and Kakeya Problems over Rings of Integers Modulo N*, arXiv:1801.03176 (2018), especially Introduction and restriction setup; https://arxiv.org/pdf/1801.03176.
2. P. Humphries, *Distributing Points on the Torus via Modular Inverses*, arXiv:2003.09955 (2020), Sections 1--3; https://arxiv.org/pdf/2003.09955.
3. G. Ricotta and E. Royer, *Kloosterman paths of prime powers moduli*, Comment. Math. Helv. 93 (2018), especially Proposition 5.4 and Section 5.2; https://www.math.u-bordeaux.fr/~gricotta/research_fichiers/version_publiee.pdf.
4. A. Bower, R. Evans, V. Luo and S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930 (2012), especially Theorem 3.6; https://arxiv.org/pdf/1212.2930.
