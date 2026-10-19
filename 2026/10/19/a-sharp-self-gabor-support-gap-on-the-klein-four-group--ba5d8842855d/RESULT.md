# A sharp self-Gabor support gap on the Klein four group

## Finding
Let \(G=\mathbb F_2^2\) with counting measure, let \(f:G\to\mathbb C\) be nonzero, and put
\[
V_ff(a,b)=\sum_{t\in G}f(t)\overline{(-1)^{b\cdot t}f(t-a)},\qquad(a,b)\in G\times G.
\]
The support cardinality is either \(4\) or at least \(6\); in particular it **cannot equal \(5\)**. The bound \(6\) is attained. All six-support cases have the following complete description:

* The support is the union of two distinct two-dimensional Lagrangian subspaces of the symplectic vector space \(G\times G\cong\mathbb F_2^4\) meeting in a one-dimensional subspace. There are exactly \(45\) such labeled supports.
* Up to multiplication by a nonzero complex scalar and application of a two-qubit Clifford unitary, every six-support signal has the form
\[
|0\rangle\otimes(\cos\theta\,|0\rangle+\sin\theta\,|1\rangle),\qquad 0<\theta<\pi/4.
\]
Conversely every such signal, and every Clifford transform of it, has self-STFT support exactly \(6\). The support-four case consists precisely of stabilizer states (equivalently, chirped coset indicators); its classification is prior theory.

## Assumptions and scope
Characters of \(G\) are identified with \(b\in G\) by \(t\mapsto(-1)^{b\cdot t}\). All inner products and supports refer to complex-valued functions on the four-element noncyclic group, and the complete \(16\)-point time-frequency plane is used. Clifford means a unitary normalizing the two-qubit Pauli/Weyl operator basis. The conclusion concerns the **self-STFT** with the signal as its own window, not arbitrary independent signal-window pairs.

## Proof
Normalize \(\|f\|_2=1\), set \(\rho=|f\rangle\langle f|\), and choose the Hermitian Pauli basis \(\{P_u:u\in W\}\) indexed by \(W=G\times G\). Its commutation form is
\[
[(a,b),(a',b')]=a\cdot b'+b\cdot a'\pmod 2.
\]
Write \(c_u=\operatorname{tr}(\rho P_u)\in\mathbb R\) and \(w_u=c_u^2\). Phases multiplying Weyl operators do not change magnitude, so \(w_u=|V_ff(u)|^2\). Pauli orthogonality gives \(w_0=1\), \(0\le w_u\le1\), and \(\sum_{u\in W}w_u=4\). Thus at least four entries are positive.

The rank-one identity \(\rho^2=\rho\), together with the commutation relation \(P_uP_vP_u=(-1)^{[u,v]}P_v\), yields the **exact symplectic Walsh eigenidentity**
\[
\sum_{v\in W}(-1)^{[u,v]}w_v=4w_u\qquad(u\in W).
\]
Indeed the left side divided by four equals \(\operatorname{tr}(\rho P_u\rho P_u)=|\operatorname{tr}(\rho P_u)|^2\). Let \(H_{u,v}=(-1)^{[u,v]}\) and \(A=H-4I_{16}\). Every actual squared-ambiguity vector is a strictly positive kernel vector of \(A\) on its exact support.

The supplied `scripts/verify_pauli_gap.py` is a finite, exhaustive **integer-arithmetic certificate**. Every support contains the origin; the program examines all \(\binom{15}{3}=455\), \(\binom{15}{4}=1365\), and \(\binom{15}{5}=3003\) candidates of sizes four, five, and six. Nonzero minors modulo \(65537\) provide valid lower bounds on characteristic-zero ranks. When the modular rank is one below full, the program constructs an **integer cofactor kernel candidate**, verifies its product with all sixteen actual integer rows, and tests strict positivity of every coordinate. This is an exact sign test, not a floating-point search. For size six and modular rank four, it explicitly verifies two independent, characteristic-zero kernel vectors.

The exact modular-rank profiles for support sizes four, five, six are, respectively,
\[
(\operatorname{rank}3:15,\ \operatorname{rank}4:440),
\quad(\operatorname{rank}4:225,\ \operatorname{rank}5:1140),
\quad(\operatorname{rank}4:45,\ \operatorname{rank}5:1440,\ \operatorname{rank}6:1518).
\]
Exactly fifteen size-four supports admit strictly positive kernel vectors: the maximal isotropic (Lagrangian) planes. No size-five support does. Exactly forty-five size-six supports do, and they are precisely the unions \(L\cup L'\) of distinct Lagrangian planes sharing a line. On any such union the two plane indicators form a basis of the real kernel, hence
\[
w=t\,\mathbf1_L+(1-t)\,\mathbf1_{L'},\qquad 0<t<1.
\]
The plane count is fifteen and each plane meets six other planes in a line, giving \(15\cdot6/2=45\) unordered unions. The enumeration and the generating symplectic geometry agree.

Let \(u\ne0\) generate the line \(L\cap L'\). Then \(w_u=1\), so equality in Cauchy–Schwarz makes \(f\) an eigenvector of the nontrivial Pauli operator \(P_u\). An elementary two-qubit Clifford unitary carries \(P_u\) to \(Z\otimes I\). Therefore the transformed state is \(|0\rangle\otimes\phi\), with a normalized one-qubit state \(\phi\). Pauli expectations of this product have support twice the number of nonzero entries among \(1,r_x,r_y,r_z\), where \((r_x,r_y,r_z)\) is the Bloch vector of \(\phi\). Because \(\|r\|_2=1\), support six means precisely two of the three Bloch coordinates are nonzero. A one-qubit Clifford permutes the coordinate axes with allowed sign changes; the remaining state can consequently be taken as \(\phi=\cos\theta|0\rangle+\sin\theta|1\rangle\), where \(0<\theta<\pi/4\). The converse follows from the same product formula. This also realizes every one of the forty-five union supports by the transitive Clifford action on pairs of Lagrangian planes meeting in a line.

## Verification
Run `python3 scripts/verify_pauli_gap.py` from the extracted package. It has no nonstandard dependencies and enumerates the complete finite support search with exact integer determinants, modular pivots, and checked integer kernel equations. Its recorded output is `verification-output.txt`. An independent direct rational example is \(f=(3/5,4/5,0,0)\), for which the nonzero ambiguity indices in the script's lexicographic \((a,b)\) convention are \(\{0,1,2,3,4,6\}\); the script recomputes the full symplectic eigenidentity over exact fractions. The finite enumeration is exhaustive for \(|G|=4\), not for any larger group.

## Relationship to prior work
Nicola's cyclic STFT uncertainty theorem (arXiv:2204.14176, 2022, Theorem 1.2) proves the minimum support and its equality classes for **cyclic** groups, and notes a partial finite-Abelian generalization. Nicola's subsequent LCA theorem (arXiv:2305.02738, 2023; *Advances in Mathematics* 451 (2024), Theorem 4.5) gives the sharp **minimum** self-ambiguity support and all minimum-support extremizers in arbitrary LCA groups, including the present support-four case. Neither theorem states the present next support threshold or classifies all support-six objects on the noncyclic four-element group. The present claim makes no assertion that support-four equality is new.

A separately reported odd-prime cyclic sharp STFT support gap concerns arbitrary signal-window pairs when the group has odd prime order at least five. Its assumptions do not include the group \(G=\mathbb F_2^2\); it cannot imply the six-support classification here. An equivalent older result under Pauli-rank or stabilizer terminology is a residual bibliographic risk.

## Limitations
This is an exact finite-dimensional classification for the **single group** \(\mathbb F_2^2\), not a theorem for all \(\mathbb F_2^d\), for cyclic groups of order four, for unequal signal-window STFTs, or for approximate/noisy support. The sharp gap is between the two smallest attainable support cardinalities only; other support sizes are not classified. The code is a finite integer certificate, and no claim of automated verification of an infinite family is made.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176 (first public 2022-04-29), Journal of Functional Analysis 284 (2023), 109924.
2. F. Nicola, *Maximally localized Gabor orthonormal bases on locally compact Abelian groups*, arXiv:2305.02738 (first public 2023-05-04), Advances in Mathematics 451 (2024), 109786, Theorem 4.5. DOI: 10.1016/j.aim.2024.109786.
