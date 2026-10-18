# The full Frobenius polynomial and rational Jacobian group of the one-point Hermitian-relative quartic

## Finding
Let \(k=\mathbb F_9\), and let \(\eta\in k\setminus\mathbb F_3\). Let \(C_\eta/k\) be the smooth projective plane quartic
\[
X^4+\eta Y^4+Y^3Z+YZ^3=0.
\]
For every choice of \(\eta\), the Hasse–Weil numerator and rational Jacobian group are
\[
\boxed{L_{C_\eta}(T)=(1-3T+9T^2)^3},\qquad
\boxed{\operatorname{Jac}(C_\eta)(\mathbb F_9)\cong(\mathbb Z/7\mathbb Z)^3}.
\]
In particular, the complete extension-field point-count formula, for every integer \(r\ge1\), is
\[
\#C_\eta(\mathbb F_{9^r})=9^r+1-2\cdot3^{r+1}\cos(r\pi/3).
\]
Equivalently, \(\operatorname{Jac}(C_\eta)\) is \(\mathbb F_9\)-isogenous to \(E^3\), where \(E\) is any elliptic curve over \(\mathbb F_9\) with Frobenius trace \(3\). This is an arithmetic isogeny statement, not an isomorphism of principally polarized abelian varieties.

## Assumptions and scope
The characteristic is exactly \(3\), the ground field is exactly \(\mathbb F_9\), and \(\eta\) ranges over \(\mathbb F_9\setminus\mathbb F_3\). The equation defines a smooth quartic: its partial derivatives are \(X^3\), \(\eta Y^3+Z^3\), and \(Y^3\), which have no common nonzero projective zero. Consequently its genus is \(g=(4-1)(4-2)/2=3\).

The 2026 classification of Hermitian-relative curves with one rational point proves that this is the unique such \(\mathbb F_9\)-projective equivalence class. For the arithmetic computation it is enough to choose an \(\eta\) satisfying \(\eta^2=-1\). Every other admissible \(\eta\) produces an \(\mathbb F_9\)-isomorphic curve by the cited classification.

## Proof
**1. Projective normalization and exact point counts.** On \(Y=0\), the defining equation forces \(X=0\), yielding exactly the point \([0:0:1]\) over every extension field. At every other projective point we may set \(Y=1\), obtaining the affine equation
\[
X^4=-\eta-Z^3-Z.
\]
For \(m=1,2,3\), construct \(K_m=\mathbb F_3[t]/(t^{2m}+t+2)\). Each modulus is irreducible: `verify.py` divides it by every monic polynomial of degrees at most \(m\), so \(K_m\) has \(3^{2m}=9^m\) elements. Choose an \(\eta_m\) with \(\eta_m^2=-1\); such an element lies in the embedded copy of \(\mathbb F_9\). The choice among the two roots does not change the result by the aforementioned equivalence.

Enumerate all \(Z\in K_m\) and count exact fourth roots of \(-\eta_m-Z^3-Z\); independently enumerate all \(X\in K_m\) and count exact solutions of \(Z^3+Z=-\eta_m-X^4\). These two exhaustive loops agree, giving

| \(m\) | \(\#C_\eta(\mathbb F_{9^m})\) | number of affine fourth-root fibres of sizes \(0,1,4\) |
|---:|---:|---|
| 1 | 1 | \((9,0,0)\) |
| 2 | 109 | \((54,0,27)\) |
| 3 | 892 | \((504,3,222)\) |

These are complete enumerations of finite fields, not statistical sampling. The field arithmetic and irreducibility checks are implemented in the standalone `verify.py`, and the precise outputs are recorded in `counts.json`.

**2. Weil reconstruction.** Write
\[
Z(C_\eta,T)=\frac{L_{C_\eta}(T)}{(1-T)(1-9T)},\qquad
L_{C_\eta}(T)=\prod_{j=1}^6(1-\alpha_jT).
\]
The three finite counts give the power sums \(s_m=\sum_j\alpha_j^m=9^m+1-\#C_\eta(\mathbb F_{9^m})\) for \(m=1,2,3\):
\[
(s_1,s_2,s_3)=(9,-27,-162).
\]
Newton's identities then give the first three nonconstant coefficients \((a_1,a_2,a_3)=(-9,54,-189)\). For a genus-three curve over \(\mathbb F_9\), the Weil functional equation determines
\[
a_4=9a_2=486,\quad a_5=9^2a_1=-729,\quad a_6=9^3=729.
\]
Therefore
\[
L_{C_\eta}(T)=1-9T+54T^2-189T^3+486T^4-729T^5+729T^6
=(1-3T+9T^2)^3.
\]
The roots \(\alpha_j\) are the two numbers \(3e^{\pm i\pi/3}\), each repeated three times, proving the point-count formula for every positive extension degree. In particular,
\[
\#\operatorname{Jac}(C_\eta)(\mathbb F_9)=L_{C_\eta}(1)=7^3=343.
\]

**3. The abstract rational group.** Let \(\pi\) denote the \(9\)-power Frobenius endomorphism on the Jacobian. Frobenius acts semisimply on its rational prime-to-\(3\) Tate modules (Tate's theorem). Its minimal polynomial is therefore the squarefree quadratic \(f(U)=U^2-3U+9\), although its characteristic polynomial is \(f(U)^3\). Hence \(f(\pi)=0\) as an actual endomorphism: the Tate-module representation is faithful. On the geometric \(7\)-torsion the reduction reads
\[
(\pi-1)(\pi-2)=0.
\]
The characteristic polynomial modulo \(7\) is \((U-1)^3(U-2)^3\), and the two roots are distinct. Thus the \(\pi=1\) eigenspace in \(\operatorname{Jac}(C_\eta)[7]\) has dimension exactly three over \(\mathbb F_7\), so its group of \(\mathbb F_9\)-rational \(7\)-torsion is \((\mathbb Z/7\mathbb Z)^3\). Since the *entire* rational Jacobian has order \(343=7^3\), this is the entire rational group.

The Tate–Honda isogeny classification (or Tate's isogeny theorem together with existence of an elliptic curve with \(\mathbb F_9\)-trace \(3\)) gives the stated \(\mathbb F_9\)-isogeny class \(E^3\).

## Verification
Run `python3 verify.py` in a directory containing that file. It has no nonstandard dependencies, checks all three irreducibility assertions by exhaustive monic-divisor trial, constructs exact characteristic-three field operations, and computes both finite affine counts independently. It verifies Newton's identities, the explicit factorization, and the Jacobian order. A successful run ends with `VERIFY_OK`. Its output is compared with `counts.json` and checks all three finite fields, including all \(729\) affine fibres of the largest one. The group structure is proved by the Frobenius argument above; the program does not enumerate Jacobian divisor classes.

## Relationship to prior work
Homma and Kim's 2024 *Relatives of the Hermitian curve* (Example 4.2 and Proposition 4.3) already displays the same equation and establishes its unique \(\mathbb F_q\)-point. No novelty is claimed for either fact. The later 2026 classification (public from May 31, 2026, with a detailed workshop presentation in June and an October preprint) establishes the unique one-point projective-equivalence class, making this genus-three arithmetic specialization canonical. The present contribution is its **complete** Weil numerator, all extension-field point counts, and exact rational Jacobian group—not a restatement of rational-point uniqueness or projective classification.

Existing general Weil and Tate theorems explain how a computed numerator controls these invariants; they do not supply the numerator for this specific curve. The inspected primary arXiv and workshop texts contain the one-point classification but not the displayed zeta polynomial. A related 2026 conference chapter is available only in preview from the consulted sources; it is a residual comparison risk. Searches of mathematical literature and indexed research records did not reveal the same computation, which is not a proof of absolute novelty.

## Limitations
This is a complete arithmetic result only for the \(\mathbb F_9\) one-point class, not an all-\(q\) formula for Hermitian-relative curves. It does not identify the Jacobian as a principally polarized product, determine its integral endomorphism ring, or establish geometric simplicity. An equivalent computation could remain unindexed or embedded in an inaccessible earlier classification chapter. The primary curve equation itself was known in 2024; the new arithmetic result is motivated by its subsequent 2026 uniqueness classification.

## References
- M. Homma and S. J. Kim, *Relatives of the Hermitian curve*, arXiv:2402.14192v2, especially Example 4.2, Proposition 4.3, and Theorem 2.5.
- M. Homma and S. J. Kim, *Classification of Hermitian-Relative Curves up to Projective Equivalence*, WAIFI 2026, first online May 31, 2026, DOI:10.1007/978-3-032-27574-5_7.
- M. Homma and S. J. Kim, *Rational points and inflexions on Hermitian-relative curves*, WCC 2026 proceedings (presentation June 11, 2026), and arXiv:2610.09672v1 (October 7, 2026).
- J.-P. Serre, *Rational Points on Curves over Finite Fields* (1985): Weil's functional equation and zeta functions.
- J. Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. 2 (1966), 134–144: semisimple Frobenius and isogeny classification.
