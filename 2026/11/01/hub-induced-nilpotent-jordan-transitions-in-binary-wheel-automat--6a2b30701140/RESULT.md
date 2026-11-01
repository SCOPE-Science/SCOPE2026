# Hub-induced nilpotent Jordan transitions in binary wheel automata

## Finding

For an integer \(n\ge3\), let \(W_n=K_1\vee C_n\) have \(n\) labelled rim vertices and one hub. For synchronous binary neighbor-XOR update \(F_n\), define \(T(x)\) as the least nonnegative number of steps after which the trajectory becomes periodic.

If \(n\) is odd, \(F_n\) is bijective and \(T(x)=0\) for every configuration.

If \(n\) is even, put \(e=2^{\nu_2(n)}\). There is a direct-sum decomposition into an invertible component of dimension \(n-e\) and a nilpotent component whose Jordan-block lengths are exactly

\[
\mathcal L_e=\begin{cases}
(3), & e=2,\\
(3,1,1), & e=4,\\
(e/2,e/2,1), & e\ge8.
\end{cases}
\]

For \(t\ge0\), let \(c_e(t)=\sum_{\ell\in\mathcal L_e}\min(t,\ell)\). Then the complete first-periodic-entry distribution is

\[
\#\{x:T(x)\le t\}=2^{n-e+c_e(t)},
\qquad
\#\{x:T(x)=0\}=2^{n-e},
\]

and for each \(t\ge1\),

\[
\#\{x:T(x)=t\}
=2^{n-e}\bigl(2^{c_e(t)}-2^{c_e(t-1)}\bigr).
\]

In particular, \(\Pr(T=0)=2^{-(e+1)}\) for uniformly random initial states. The maximum first-entry time is exactly \(3\) when \(e=2\) or \(4\), and \(e/2\) when \(e\ge8\). All probabilities depend only on \(e\), not on the odd factor of \(n\).

## Assumptions and scope

The ring \(C_n\) is the simple undirected cycle of \(n\ge3\) vertices, and \(W_n\) has exactly \(n+1\) vertices. Configurations are vectors over \(\mathbb F_2\). Every site updates simultaneously using the exclusive-or sum of its neighbors, excluding its own state. A state is *periodic* when some strictly positive iterate returns to it; the least time at which the trajectory reaches such a state is \(T(x)\). Counts are of labelled configurations, not orbits modulo symmetry. No assertion about the lengths of the eventual periodic cycles is needed.

## Proof

Write the rim state as a residue polynomial \(f\) in \(R=\mathbb F_2[z]/(z^n+1)\), and the hub state as \(h\in\mathbb F_2\). Put \(S=\sum_{i=0}^{n-1}z^i\), \(b=z+z^{-1}=z^{-1}(z+1)^2\), and \(\varepsilon(f)=f(1)\). The update is exactly

\[
F_n(f,h)=(bf+hS,\varepsilon(f)).
\]

The identities \(bS=0\) and \(\varepsilon(bf)=0\) hold in every characteristic-two quotient of this form. Also \(\varepsilon(S)=n\bmod2\).

**Odd circumference.** If \(n\) is odd and \(F_n(f,h)=0\), applying \(\varepsilon\) to the rim equation gives \(h=0\). Because \(z^n+1\) has a simple factor \(z+1\), the kernel of multiplication by \(b\) is the one-dimensional space spanned by \(S\). The hub equation gives \(\varepsilon(f)=0\), hence \(f=0\). Thus \(F_n\) is injective and therefore bijective on its finite state space. Every state of a finite permutation is periodic.

**Even circumference and primary decomposition.** Write \(n=eq\) with \(e=2^{\nu_2(n)}\ge2\) and \(q\) odd. In \(\mathbb F_2[z]\),

\[
z^n+1=(z^q+1)^e=(z+1)^e g(z)^e,
\qquad g(1)=1.
\]

The Chinese remainder theorem decomposes \(R=R_0\oplus R_*\), where \(R_0=\mathbb F_2[u]/(u^e)\) with \(u=z+1\), and \(R_*\) is the complementary factor. Multiplication by \(b=z^{-1}u^2\) is invertible on \(R_*\). Both the augmentation \(\varepsilon\) and coupling polynomial \(S\) are zero on \(R_*\); in \(R_0\), \(S=u^{e-1}\). Therefore \(F_n\) splits into an invertible part on \(R_*\), of dimension \(n-e\), and a nilpotent part on \(R_0\oplus\mathbb F_2\), of dimension \(e+1\).

For even \(n\), the identities above give exact iterates

\[
F_n^2(f,h)=(b^2f+S\varepsilon(f),0),\qquad
F_n^t(f,h)=(b^tf,0)\quad(t\ge3).
\]

These formulas also show that the local part is nilpotent, since the local multiplier \(b\) is \(u^2\) times a unit.

**Jordan ranks.** On \(R_0\oplus\mathbb F_2\), denote \(r_t=\operatorname{rank}(F_n^t)\), with \(r_0=e+1\). For \(e=2\), \(b=0\) locally and the two output coordinates \(hu\) and \(\varepsilon(f)\) are independent. Consequently

\[
(r_0,r_1,r_2,r_3)=(3,2,1,0).
\]

For \(e\ge4\), the rim output of the first iterate belongs to \(u^2R_0\), and its coefficient of \(u^2\) determines \(\varepsilon(f)\); since \(hu^{e-1}\) has degree at least three, the hub output does not increase the rank. Hence \(r_1=e-2\). For \(e=4\), multiplication by \(b^2\) vanishes, while \(S\varepsilon\) has rank one. Thus

\[
(r_0,r_1,r_2,r_3)=(5,2,1,0).
\]

For \(e\ge8\), multiplication by \(b^2\) maps onto \(u^4R_0\). The added term \(u^{e-1}\varepsilon(f)\) changes only a strictly higher coefficient in the resulting upper-triangular matrix and leaves its rank \(e-4\). Thus \(r_2=e-4\). For every \(t\ge3\), multiplication by \(b^t\) has image \(u^{2t}R_0\), giving

\[
r_t=\max(e-2t,0)\quad(t\ge3).
\]

For a nilpotent matrix, the number of Jordan blocks of length at least \(t\) is \(r_{t-1}-r_t\). Substituting the preceding complete rank profiles gives, respectively, \((3)\), \((3,1,1)\), and \((e/2,e/2,1)\). This establishes the claimed nilpotent block partition for all even \(n\).

**First-entry census.** By the Fitting decomposition, a state is periodic exactly when its nilpotent coordinate vanishes: a nonzero vector in a nilpotent space cannot be periodic, and every vector in an invertible finite-field component is periodic. Thus \(T(x)\le t\) if and only if its nilpotent coordinate lies in \(\ker(F_n^t)\). The latter kernel has dimension \(c_e(t)\), while the free invertible component contributes \(n-e\) binary dimensions. This proves the cumulative count. Subtracting consecutive cumulative counts gives each shell. At \(t\) equal to the largest block length, \(c_e(t)=e+1\), so the shells exhaust the \(2^{n+1}\) states; at smaller times the kernel is proper. Therefore the maximum time is sharp.

## Verification

Run `python verify_wheel_xor.py` with Python 3. The standalone script directly constructs simple wheel edges as binary adjacency masks, computes matrix ranks and microscopic neighbor-XOR trajectories, and compares with the formulas. Its recorded output is `verification_output.txt`. It checked all ring sizes \(3\le n\le128\) by binary matrix-power ranks (585 rank comparisons) and completely traversed the \(262128\) labelled configurations for \(3\le n\le16\). These finite checks corroborate, but do not replace, the preceding infinite-family proof.

For illustration, the first-entry shells at \(n=4\) are \((1,7,8,16)\), and at \(n=8\) are \((1,7,24,96,384)\), listed from \(t=0\) onward.

## Relationship to prior work

Rowland and Yassawi's work on linear cellular automata over finite fields includes the neighbor-XOR Rule 90 framework and establishes results about automatic spacetime columns; it does not give a finite-wheel nilpotent Jordan partition or first-periodic-entry law. Abu-Jeib previously obtained the **integer determinant and real spectrum** of wheel adjacency matrices; in particular, the prior even-order determinant identity already implies the invertibility half of the odd-rim criterion modulo two. That invertibility observation alone is **not claimed as new**. Fran, Saputri and Kiftiah investigated products of wheel adjacency matrices modulo two and their graphical realizability, but not the all-power Jordan partition or the resulting stopping-time distribution. The new mathematical content assessed here is the explicit complete characteristic-two nilpotent structure in all three dyadic regimes and its exact finite-dynamics entry census.

## Limitations

The result counts first-entry times, not the multiplicities or exact lengths of the eventual periodic orbits in the invertible component. It concerns precisely the loopless neighbor-sum rule on simple wheel graphs; it does not cover asynchronous or nonlinear majority updates, other finite fields, or arbitrary graph joins. Prior art that derives the same modular Jordan partition from wheel adjacency spectra could subsume the conclusion even without stating stopping times; that possibility requires further historical scrutiny. Independent external audit has not been performed.

## References

1. Eric Rowland and Reem Yassawi, *A characterization of p-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008v1, submitted 2012-09-26; full text: https://arxiv.org/html/1209.6008v2.
2. Iyad T. Abu-Jeib, *The Determinant of the Wheel Graph and Conjectures by Yong*, Missouri Journal of Mathematical Sciences **18** (2006); DOI: 10.35834/2006/1802142; full text: https://www.aaup.edu/sites/default/files/2017-07/abujeib11_conjectures.pdf.
3. Fransiskus Fran, Novita Indah Saputri and Mariatul Kiftiah, *Hasil Kali Matriks (Mod 2) pada Graf Roda, Graf Pertemanan dan Graf Bunga*, Jambura Journal of Mathematics **3** (2021), 167–179; DOI: 10.34312/jjom.v3i2.10468; https://ejurnal.ung.ac.id/index.php/jjom/article/view/10468.
