# Brauer vanishing for split-quadric Enriques quotients in every even dimension at least four

## Finding
For every even integer \(n\ge 4\), let \(Y\subset\mathbb P^{2n+1}_{\mathbb C}\) be a smooth complete intersection of \(n+1\) split quadrics
\[
Q_j(x_0,\ldots,x_n)+\widetilde Q_j(y_0,\ldots,y_n)=0,\qquad 1\le j\le n+1,
\]
whose intersection with both coordinate \(\mathbb P^n\)'s is empty. Such intersections occur for general choices of the quadrics [2]. The involution \(\iota([x:y])=[-x:y]\) therefore acts freely on \(Y\). Write \(T=Y/\langle\iota\rangle\), and write \(h\) for its descended hyperplane class.

The integral low-degree cohomology and geometric groups are
\[
\begin{aligned}
\pi_1(T)&\simeq \mathbb Z/2, & H^1(T,\mathbb Z)&=0,\\
H^2(T,\mathbb Z)&\simeq\mathbb Z\oplus\mathbb Z/2, & H^3(T,\mathbb Z)&=0,\\
\operatorname{Pic}(T)&\simeq\mathbb Z\langle h\rangle\oplus(\mathbb Z/2)\langle K_T\rangle,
& \operatorname{Br}(T)&=0.
\end{aligned}
\]
In particular, every algebraic Azumaya Brauer class on \(T\) is trivial, although \(K_T\) is a nontrivial line bundle of order two. The vanishing sharply contrasts with the classical dimension-two Enriques-surface case, where the Brauer group is \(\mathbb Z/2\) [1].

## Assumptions and scope
All varieties and cohomology groups are over \(\mathbb C\); singular cohomology uses integral coefficients. The intersection \(Y\) is assumed smooth and the above coordinate fixed loci disjoint from it. These conditions hold for general split quadrics [2, Section 6.1.5]. The claim covers each even \(n\ge4\), not the case \(n=2\), and does not claim anything about singular or non-free quotients. The Brauer group denotes the algebraic Brauer group; its cohomological and analytic incarnations also vanish here.

## Proof
**1. The cover in degrees below four.** The dimension of \(Y\) is \(n\). The integral Lefschetz hyperplane theorem for smooth complete intersections identifies \(H^q(Y,\mathbb Z)\) with \(H^q(\mathbb P^{2n+1},\mathbb Z)\) for every \(q<n\); the Lefschetz theorem on fundamental groups also gives \(\pi_1(Y)=0\). Since \(n\ge4\),
\[
H^0(Y,\mathbb Z)=\mathbb Z,\quad H^1(Y,\mathbb Z)=0,\quad H^2(Y,\mathbb Z)=\mathbb Z\langle c_1(\mathcal O_Y(1))\rangle,\quad H^3(Y,\mathbb Z)=0.
\]
The involution preserves \(\mathcal O_Y(1)\), so its action on the one-dimensional \(H^2\) is trivial. It also acts trivially on \(H^0\). The free double quotient has \(\pi_1(T)=\mathbb Z/2\).

**2. Cartan–Leray page and all possible low-degree differentials.** Put \(G=\langle\iota\rangle\cong\mathbb Z/2\). The integral Cartan–Leray spectral sequence for the free action is
\[
E_2^{p,q}=H^p(G,H^q(Y,\mathbb Z))\Longrightarrow H^{p+q}(T,\mathbb Z).
\]
For the trivial integral \(G\)-module \(\mathbb Z\), the standard periodic cyclic-group resolution gives
\[
H^p(G,\mathbb Z)=\begin{cases}
\mathbb Z,&p=0,\\
\mathbb Z/2,&p>0\text{ even},\\
0,&p\text{ odd}.
\end{cases}
\]
Because the rows \(q=1\) and \(q=3\) vanish, every second-page term of total degree \(3\) is zero: \(E_2^{0,3}=E_2^{1,2}=E_2^{2,1}=E_2^{3,0}=0\). Therefore \(H^3(T,\mathbb Z)=0\).

In total degree \(2\), the only nonzero terms are \(E_2^{0,2}=\mathbb Z\) and \(E_2^{2,0}=\mathbb Z/2\). The only possible nontrivial outgoing differential from \((0,2)\) is \(d_3:E_3^{0,2}\to E_3^{3,0}\), but the target is zero; the \(d_2\) target \((2,1)\) is also zero. Neither term can receive a nonzero incoming differential, and \((2,0)\) has no nonzero outgoing differential. Thus both survive to \(E_\infty\), and the filtration yields
\[
0\longrightarrow\mathbb Z/2\longrightarrow H^2(T,\mathbb Z)\longrightarrow\mathbb Z\longrightarrow0.
\]
This splits because \(\mathbb Z\) is free. The integral \(H^1\) group vanishes for the same page reasons.

**3. Picard and Brauer groups.** Since \(Y\) is a Calabi–Yau complete intersection of dimension at least four, \(H^1(Y,\mathcal O_Y)=H^2(Y,\mathcal O_Y)=0\); this also follows from the Hodge decomposition and the preceding Lefschetz computation. The finite étale map \(Y\to T\) makes \(H^i(T,\mathcal O_T)\) a direct summand of \(H^i(Y,\mathcal O_Y)\) in characteristic zero. Thus these two sheaf-cohomology groups vanish on \(T\) as well. The exponential exact sequence then identifies \(c_1:\operatorname{Pic}(T)\to H^2(T,\mathbb Z)\) as an isomorphism and forces \(H^2(T,\mathcal O_T^*)=0\), since the next term is \(H^3(T,\mathbb Z)=0\). Consequently the analytic cohomological Brauer group and the algebraic Brauer group both vanish.

The involution on ambient homogeneous coordinates has determinant \((-1)^{n+1}=-1\), while it fixes each defining quadratic equation. Its action on a holomorphic residue generator of \(H^0(Y,\omega_Y)\) is therefore \(-1\). Thus \(\omega_T\) is a nontrivial line bundle of order two. This identifies the unique torsion summand of \(\operatorname{Pic}(T)\). The linearized \(\mathcal O_Y(1)\) descends to a line bundle \(h\) on \(T\); its pullback is the primitive hyperplane class in \(H^2(Y,\mathbb Z)\). The edge map in Step 2 is surjective, so \(h\) generates the free summand.

## Verification
The relevant second-page groups in total degrees at most three and all possible incoming/outgoing differentials have been enumerated explicitly in Step 2. The accompanying standard-library script \(\texttt{low_degree_check.py}\) checks the group-cohomology parity table and verifies that the four total-degree-three positions vanish and the two total-degree-two positions have types \(\mathbb Z\) and \(\mathbb Z/2\). This finite structural check does **not** substitute for integral Lefschetz, the Cartan–Leray convergence theorem, or the exponential exact sequence, on which the universal conclusion depends.

## Relationship to prior work
Frassineti–Rizzo–Tufo–Verni [1], first posted 6 May 2026, study Brauer groups of Enriques manifolds with **hyper-Kähler** universal cover, and introduce the relevant Cartan–Leray and Brauer comparison tools. Their Theorems and Section 3 do not determine the Brauer group of the **Calabi–Yau** split-quadric quotients considered here. Boissière–Camere–Sarti [2], originally posted 13 September 2024, explicitly construct this family in Section 6.1.5 and discuss its canonical double cover, but do not report the integral third cohomology or the Brauer-group calculation. Their general torsion-canonical results already cover the existence and order of \(K_T\), and those facts alone are **not asserted as new**. The specific value \(\operatorname{Br}(T)=0\), established uniformly for every even \(n\ge4\) along with the low-degree integral groups, is the distinct claim made here.

## Limitations
The result applies only to smooth fixed-point-free members and even dimensions at least four. It does not identify integral cohomology in middle or higher degrees, compute derived-category Brauer phenomena, classify all Enriques manifolds, or assert priority over every unindexed source. The proof uses standard topological theorems rather than a new general spectral-sequence method; the contribution is the precise application and uniform geometric classification of the natural Brauer invariant for this family.

## References
[1] A. Frassineti, F. Rizzo, F. Tufo, M. Verni, *On Brauer groups of known Enriques manifolds*, arXiv:2605.05450v1 (6 May 2026), Introduction and Sections 2–3. https://arxiv.org/abs/2605.05450

[2] S. Boissière, C. Camere, A. Sarti, *Logarithmic Enriques varieties*, arXiv:2409.09160v1 (13 September 2024), Section 6.1.5 and the discussion of torsion canonical classes. https://arxiv.org/abs/2409.09160
