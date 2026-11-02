# The first three-witness genus for one-pointed linear Hodge denominators

## Finding

For each integer \(g\ge 1\) and \(0\le i\le g\), define the rational intersection number
\[
H_{g,i}=\int_{\overline{\mathcal M}_{g,1}}\psi_1^{2g-2+i}\lambda_{g-i}.
\]
Write \(d_{g,i}\) for the positive denominator of \(H_{g,i}\) in lowest terms, and \(T_{2g}\) for the Minkowski number with
\[
\nu_p(T_{2g})=\sum_{j\ge 0}\left\lfloor\frac{2g}{(p-1)p^j}\right\rfloor
\qquad(p\text{ prime}).
\]
The *denominator witness number* is the minimum size of a subset of these \(g+1\) specified intersection numbers whose denominator least common multiple is \(T_{2g}\):
\[
w_g=\min\left\{|I|: I\subseteq\{0,\ldots,g\},\quad
\operatorname{lcm}_{i\in I}d_{g,i}=T_{2g}\right\}.
\]
The minimum exists because the full least common multiple equals \(T_{2g}\), as proved by Holmes.

**Exact cutoff theorem.** In genera \(1\le g\le10\), the complete sequence of minima is
\[
\boxed{(w_1,w_2,\ldots,w_{10})=(1,1,2,2,1,2,2,2,2,3).}
\]
Consequently, genus \(10\) is the **first genus in this one-pointed linear family** in which at least three different Hodge integrals are indispensable for witnessing the full universal denominator. The three indices \(\{0,1,3\}\) suffice in genus \(10\).

For reference, sharp witnesses in each genus are:

| \(g\) | \(w_g\) | One minimizing index set \(I\) |
| ---: | ---: | :--- |
| 1 | 1 | \(\{0\}\) |
| 2 | 1 | \(\{0\}\) |
| 3 | 2 | \(\{0,1\}\) |
| 4 | 2 | \(\{0,1\}\) |
| 5 | 1 | \(\{1\}\) |
| 6 | 2 | \(\{0,2\}\) |
| 7 | 2 | \(\{0,3\}\) |
| 8 | 2 | \(\{0,2\}\) |
| 9 | 2 | \(\{0,3\}\) |
| 10 | 3 | \(\{0,1,3\}\) |

## Assumptions and scope

All integrals are ordinary rational intersection numbers on the complex Deligne–Mumford stack of stable one-pointed curves; \(\lambda_0=1\). This is **not** a claim about the fewest arbitrary Hodge integrals (allowing more markings, nonlinear products of Hodge classes, or changing the genus) needed for the Minkowski denominator. The theorem is a sharp finite-genus classification, not a conjectural extrapolation beyond genus \(10\).

## Proof

**Step 1: coefficient identity.** Faber and Pandharipande's Theorem 2 gives the formal identity
\[
\left(\frac{t/2}{\sin(t/2)}\right)^{x+1}
=1+\sum_{g\ge1}t^{2g}\sum_{i=0}^g H_{g,i}x^i.
\]
The coefficient of \(t^{2g}x^i\) is therefore *exactly* the stated intersection number. In particular no numerical integration or floating-point approximation enters the proof.

**Step 2: two rational constructions.** Let \(z=t^2\), and set
\[
L(z)=\log\left(\frac{\sqrt z/2}{\sin(\sqrt z/2)}\right)
=\sum_{j\ge1}c_jz^j,
\qquad c_j=\frac{(-1)^{j-1}B_{2j}}{2j(2j)!}.
\]
The Bernoulli numbers are defined by \(t/(e^t-1)=\sum_{m\ge0}B_mt^m/m!\). Defining \(P_g(x)=[z^g]\exp(xL(z))\), differentiation shows that the coefficient \(q_{g,k}=[x^k]P_g(x)\) obeys
\[
q_{0,0}=1,\qquad
q_{g,k}=\frac1g\sum_{j=1}^{g}j c_jq_{g-j,k-1}\quad(g\ge1),
\]
with out-of-range coefficients zero. Finally \(H_{g,i}=[x^i]P_g(x+1)\).

For independent verification, expand
\[
A(z)=\frac{\sin(\sqrt z/2)}{\sqrt z/2}
=\sum_{j\ge0}\frac{(-1)^jz^j}{2^{2j}(2j+1)!},
\]
form its exact formal reciprocal, evaluate \([z^g]A(z)^{-r}\) for each integer \(1\le r\le g+1\), and interpolate the unique polynomial \([z^g]A(z)^{-(x+1)}\) of degree at most \(g\). The two constructions give identical rational coefficients in every genus from \(1\) through \(10\).

**Step 3: exhaustive finite sharpness.** Reduce the exact rational coefficients; compute their positive denominators and independently compute the prescribed prime powers of \(T_{2g}\). For each \(1\le g\le10\), first verify
\(\operatorname{lcm}_{0\le i\le g}d_{g,i}=T_{2g}\). Then enumerate **every** nonempty subset of \(\{0,\ldots,g\}\), in increasing size, and compare its denominator least common multiple with \(T_{2g}\). The first successful subset size is precisely the value \(w_g\) in the table. This checks all proper candidate subsets, not a sample.

**Step 4: structural obstruction at the first three-witness genus.** At \(g=10\),
\[
T_{20}=2^{38}\cdot3^{14}\cdot5^{6}\cdot7^{3}\cdot11^{2}\cdot13\cdot17\cdot19
=3579998068407778230140928000000.
\]
Among the eleven coefficients \(H_{10,i}\), the exact sets of indices whose denominators reach each of three crucial full prime powers are
\[
\begin{aligned}
S_{3^{14}}&=\{3,4,9,10\},\\
S_{5^6}&=\{1,5\},\\
S_{19}&=\{0,2\}.
\end{aligned}
\]
These sets are pairwise disjoint, so an index subset whose denominators collectively reach all three prime powers must have at least **three** elements. Conversely, the denominators at \(i=0,1,3\) jointly have maximum valuations \((38,14,6,3,2,1,1,1)\) at the primes \((2,3,5,7,11,13,17,19)\), equal to the valuations of \(T_{20}\). Thus \(w_{10}=3\), independently of any exhaustive subset search. The smaller-genus witness counts are established by the exact exhaustive finite computation of Step 3. \(\square\)

## Verification

The attached file `verify.py` uses Python's standard library and *exact* integer/rational arithmetic. Run `python3 verify.py`. It constructs the entire coefficient array through genus \(10\) twice, compares the arrays entrywise, verifies the full Minkowski least common multiple for every genus, exhausts the subsets determining each minimum, and checks the pairwise-disjoint genus-ten support sets. A machine-readable record of all denominators and exact genus-ten rational values is in `certificate.json`. The script terminates with `VERIFY_OK` on success. All loops and coefficient ranges relevant to the theorem are finite and explicitly bounded; this does not certify anything about genera \(g\ge11\).

## Relationship to prior work

Faber–Pandharipande's 1998 Theorem 2 provides all the rational numbers in the linear one-pointed family by a trigonometric generating series. Holmes's 2026 Theorem 1.4 and Proposition 3.8 show that their total denominator least common multiple realizes the universal genus-\(g\) Minkowski number. Neither of these inspected statements determines the **smallest number of individual coefficients** required, the first genus in which two cannot suffice, or the three pairwise-incompatible full-prime-power support sets exhibited above. The result refines the *witness complexity* of that pre-existing exact denominator theorem; it does not reprove or claim ownership of the generating series, the Minkowski formula, or universal denominator equality.

Older results of Carlitz, Adelberg and others on Nørlund-polynomial coefficient denominators are mathematically related. Those statements may imply partial or implicit coefficient-wise information after a change of variables; full historical priority is not established by the present searches.

## Limitations

The first-genus statement refers only to \(H_{g,i}\) as defined above. The arithmetic procedure is exhaustive only for \(1\le g\le10\); no structural law for later genera is proved. The denominator-witness invariant is computationally accessible from the known Faber–Pandharipande formula, and it is possible that the exact small-genus classification is already implicit or tabulated in earlier arithmetic treatments of Nørlund polynomials. No independent mathematical validation has been performed.

## References

- C. Faber and R. Pandharipande, *Hodge integrals and Gromov–Witten theory*, arXiv:math/9810173v1 (publicly posted October 30, 1998), Theorem 2. https://arxiv.org/html/math/9810173v1
- D. Holmes, *Denominators of Hodge integrals and Minkowski numbers*, arXiv:2610.30274v1 (publicly posted October 21, 2026), Theorem 1.4 and Proposition 3.8. https://arxiv.org/html/2610.30274v1
- A. Adelberg, *Arithmetic properties of the Nörlund polynomial*, Discrete Mathematics 204 (1999), 5–13; doi:10.1016/S0012-365X(98)00363-X (comparison made from accessible abstract).
