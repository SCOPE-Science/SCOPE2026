# Uniform local conditioning is necessary for a continuous \(g\)-weaving equivalence

## Finding
Theorem 2.7 of Alizadeh--Sadri asserts an equivalence between continuous \(g\)-weaving of operator families and continuous weaving of the vector families obtained by inserting local continuous frames into the coefficient spaces.

The statement allows the local frame bounds to depend on the outer index. Its proof then sets
\[
A=\inf_{\omega,i}\{A_{F_{\omega i}},A_{G_{\omega i}}\}
\]
and
\[
B=\sup_{\omega,i}\{B_{F_{\omega i}},B_{G_{\omega i}}\}
\]
and divides or multiplies by these quantities. The theorem does not assume
\[
A>0
\qquad\text{or}\qquad
B<\infty.
\]
Both omissions are substantive.

For the first direction, take
\[
H=\ell^2(\mathbb N),
\qquad
\Omega=\mathbb N
\]
with counting measure and \(H_n=\mathbb C\). Make all weave labels identical and define
\[
\Lambda_{n,i}f=\Theta_{n,i}f=f_n.
\]
Every outer weave is Parseval. For each \(n\), use a one-point local frame in \(\mathbb C\),
\[
F_{n,i}(*)=G_{n,i}(*)=\frac1n.
\]
Each local frame has bounds \(1/n^2\), but their lower-bound infimum is zero. The induced vectors are
\[
\frac1n e_n.
\]
Their frame energy is
\[
\sum_{n=1}^{\infty}\frac{|f_n|^2}{n^2},
\]
which has no positive lower bound. Thus continuous \(g\)-weaving need not imply weaving of the induced vectors.

For the reverse direction, define instead
\[
\Lambda_{n,i}f=\Theta_{n,i}f=\frac{f_n}{n}
\]
and take
\[
F_{n,i}(*)=G_{n,i}(*)=n.
\]
The local frame bounds are \(n^2\), so their supremum is infinite. The induced vectors are exactly
\[
e_n,
\]
hence every induced weave is Parseval, but the outer operator families again have energy
\[
\sum_{n=1}^{\infty}\frac{|f_n|^2}{n^2}
\]
and are not \(g\)-frames.

A correct uniform theorem requires constants
\[
0<a\le b<\infty
\]
that bound every local frame from below and above.

## Assumptions and scope
The counterexamples use a discrete measure space, which is a legitimate special case of the continuous definitions because counting measure is allowed.

Each coefficient space is one-dimensional. The local continuous frames are one-point frames, so there are no hidden measurability or convergence issues in the inner variable.

All weave labels are chosen identical. Therefore every partition produces the same energy, and the failure is caused only by the nonuniform local frame conditioning, not by a pathological partition.

The finding concerns the equivalence theorem. It does not assert that a particular nonuniform collection can never satisfy the equivalence through compensating structure.

## Proof
Let \(E_g(f)\) denote the energy of a fixed outer operator weave, and let \(E_{\mathrm{vec}}(f)\) denote the energy after applying the corresponding local continuous frames.

For each outer index, the local frame inequality has the form
\[
A_{\omega,i}\|\Lambda_{\omega,i}f\|^2
\le
\int |\langle \Lambda_{\omega,i}f,F_{\omega,i}(x)\rangle|^2\,d\mu(x)
\le
B_{\omega,i}\|\Lambda_{\omega,i}f\|^2,
\]
and analogously for the other woven family.

If
\[
0<a\le A_{\omega,i}
\quad\text{and}\quad
B_{\omega,i}\le b<\infty
\]
uniformly over every local frame occurring in either family, integration over the outer index gives
\[
aE_g(f)\le E_{\mathrm{vec}}(f)\le bE_g(f).
\]

If the outer weave has bounds \(C,D\), then
\[
aC\|f\|^2
\le
E_{\mathrm{vec}}(f)
\le
bD\|f\|^2.
\]
Conversely, if the induced vector weave has bounds \(C,D\), then
\[
E_{\mathrm{vec}}(f)\le bE_g(f)
\]
and
\[
aE_g(f)\le E_{\mathrm{vec}}(f)
\]
give
\[
\frac{C}{b}\|f\|^2
\le
E_g(f)
\le
\frac{D}{a}\|f\|^2.
\]

For the first counterexample, taking \(f=e_N\) gives induced energy
\[
\frac1{N^2},
\]
so no positive lower frame bound exists.

For the second counterexample, taking \(f=e_N\) gives outer energy
\[
\frac1{N^2},
\]
so again no positive lower frame bound exists, while the induced family is the standard orthonormal basis.

Thus uniform positive lower local bounds and uniform finite upper local bounds are exactly what the published proof needs for its two directions.

## Verification
The statement and proof of Theorem 2.7 were inspected in the publicly available full-text rendering of the 2020 article. The theorem gives local frame bounds for each outer coefficient space, while the proof introduces their global infimum and supremum without a uniformity hypothesis.

A later open-access Hilbert \(C^*\)-module extension was inspected in its version-of-record PDF. Its Theorem 0.12 repeats the same equivalence. On the theorem page, the proof again sets an infimum of local lower bounds and a supremum of local upper bounds; the following page completes the two transfers using those quantities.

The two counterexamples above are exact. Each local one-point system is a genuine frame of \(\mathbb C\), every outer or induced energy is computed by a diagonal series, and failure of a lower frame bound is witnessed by the standard unit vectors.

## Relationship to prior work
The 2020 article was available online on 7 August 2020 and lists 42C15 first in its classification.

An earlier continuous weaving fusion-frame construction uses fixed local frame bounds in its analogous passage from local frames to fusion data, so it does not supply the pointwise-varying hypothesis that creates the present defect.

The 2023 Hilbert \(C^*\)-module extension reproduces the pointwise-bound statement and the same infimum/supremum proof mechanism. Its persistence makes the uniformity issue relevant beyond a single notation choice.

Searches using the exact theorem number, DOI, local-frame-bound formulation, infimum/supremum formulation, and correction terminology did not locate an indexed correction containing the two counterexamples or the quantitative repaired equivalence.

## Limitations
The repaired theorem gives a clean uniform sufficient condition and quantitative transfer of bounds. It does not classify all specially correlated nonuniform local systems for which the equivalence may still happen to hold.

The two examples establish that neither uniform lower control nor uniform upper control can be dropped from a theorem meant to cover arbitrary local-frame fields.

A nonindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. E. Alizadeh and V. Sadri, *On Continuous Weaving G-Frames in Hilbert Spaces*, Wavelets and Linear Algebra 7(1) (2020), 23--36, DOI 10.22072/wala.2020.114423.1248.
2. N. Assila, M. Ghiati, M. Mouniane and M. Rossafi, *Continuous weaving \(g\)-frames in Hilbert \(C^*\)-modules*, Jurnal Matematika, Statistika dan Komputasi 19(3) (2023), 563--579, DOI 10.20956/j.v19i3.25230.
3. V. Sadri, R. Ahmadi and G. Rahimlou, *On continuous weaving fusion frames in Hilbert spaces*, arXiv:1901.03799v1.
