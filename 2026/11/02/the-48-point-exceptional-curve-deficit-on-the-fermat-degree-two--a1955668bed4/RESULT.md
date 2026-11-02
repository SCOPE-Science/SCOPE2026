# The 48-point exceptional-curve deficit on the Fermat degree-two del Pezzo surface over \(\mathbb F_{25}\)

## Finding
For \(k=\mathbb F_{25}=\mathbb F_5[\theta]/(\theta^2-2)\), consider the smooth degree-two del Pezzo surface
\[
S:\quad w^2=x^4+y^4+z^4\subset\mathbb P_k(1,1,1,2).
\]
All its 56 exceptional curves are \(k\)-rational. Their union \(E\) satisfies
\[
\#S(k)=826,\qquad \#E(k)=778,\qquad\#(S(k)\setminus E(k))=48.
\]
The 48 uncovered points project two-to-one to a set of 24 plane points: each has exactly one zero coordinate, and the fourth power of the ratio of its other two coordinates is a nonidentity cube root of unity. This 24-point locus is one orbit under coordinate permutations and multiplication by fourth roots of unity; its 48 lifts form one orbit after adjoining the deck involution. Thus the natural split Fermat surface is not *full* over \(\mathbb F_{25}\).

## Assumptions and scope
The base field is exactly \(\mathbb F_{25}\), with characteristic 5; \(w\) has weight 2 and \(x,y,z\) weight 1. Let \(C:\ x^4+y^4+z^4=0\) be the smooth plane branch quartic. An exceptional curve means a geometric smooth rational curve of self-intersection \(-1\) on \(S\). A *full* split degree-two del Pezzo surface is one whose rational points all lie on its 56 exceptional curves. No claim is made about all split degree-two del Pezzo surfaces over \(\mathbb F_{25}\), or the situation in other field degrees.

## Proof
**1. Smooth surface and bitangents.** The gradient of the homogeneous equation of \(C\) is \((4x^3,4y^3,4z^3)\); it has no projective zero. As 2 is invertible, the double cover \(S\to\mathbb P^2\) branched over \(C\) is smooth and is a degree-two del Pezzo surface. For a smooth plane quartic in odd characteristic, the 28 geometric bitangents correspond to the 56 geometric exceptional curves, paired over each bitangent.

Let \(\mu_4\subset k^\times\) denote the fourth roots of unity, and choose \(\theta^2=2\). Since \(\mu_4=\mathbb F_5^\times\), the 16 distinct lines
\[
L_{a,b}:\quad x+ay+bz=0,\qquad a,b\in\mu_4,
\]
are bitangents: substituting the line equation, one has the polynomial identity
\[
(-ay-bz)^4+y^4+z^4
=\left[\theta(a^2y^2+b^2z^2)+(2ab/\theta)yz\right]^2.
\]
The quadratic factor has nonzero discriminant \(4a^2b^2\), giving two distinct contacts. There are another twelve distinct lines
\[
x=\alpha y,\quad x=\alpha z,\quad y=\alpha z,
\qquad \alpha^4=-1;
\]
on each, the quartic restricts to the fourth power of the remaining coordinate. They are hyperflex bitangents. The roots of \(t^4=-1\) all lie in \(k\) since \(8\mid 24\). These 28 distinct lines exhaust all geometric bitangents, and their square-root restrictions lie in \(k\); hence every one of the 56 exceptional curves is defined over \(k\). The number of rational surface points lying above a base point is two for a nonzero square branch value, one for branch value zero, and zero for a nonsquare.

**2. Exact finite partition.** Normalize points of \(\mathbb P^2(k)\) by making the last nonzero coordinate equal to 1. There are \(25^2+25+1=651\) representatives. The accompanying standalone verifier evaluates the quartic, its square status, and membership in the 28 explicit bitangent lines for **every** representative using only integer pairs modulo 5 in \(k=\mathbb F_5[\theta]/(\theta^2-2)\). The resulting rational-point incidence histogram, classified by the number of bitangent lines through the base point, is
\[
\begin{array}{c|rrrrr}
\text{bitangents through image}&0&1&2&3&4\\\hline
\text{surface rational points}&48&236&480&32&30
\end{array}.
\]
Thus there are exactly \(826\) surface points, of which \(778\) lie on the 56 exceptional curves. On any bitangent, the full rational fibre lies in the union of its two \(k\)-rational exceptional components, including contact points; outside the bitangents the fibre cannot meet an exceptional curve.

**3. Complete description of the deficit.** The verifier independently constructs the set of all projected points having exactly one zero coordinate and ratio \(t\) between the two nonzero coordinates with \(t^4\in\mu_3\setminus\{1\}\). It proves set equality with the projected uncovered locus, yielding exactly 24 base points (8 per coordinate axis), each with two rational lifts. The reduction is also transparent on each axis: \(t^4\) belongs to \(\mu_6\). For \(t^4=1\), there is an ordinary bitangent; for \(t^4=-1\), a hyperflex; for \(t^4\in\mu_3\setminus\{1\}\), the branch value \(1+t^4\) is a nonzero square but no bitangent passes through the point; for the two remaining primitive-sixth-root classes, \(1+t^4\) is a nonsquare (its norm to \(\mathbb F_5\) is 3). For points with all coordinates nonzero, a complete 36-class check by \((x^4/z^4,y^4/z^4)\in\mu_6^2\) shows that every rational fibre is on a bitangent; each class has 16 base representatives. All checks are exhaustive, not a sample.

For orbit transitivity, diagonal multiplication by \(\mu_4\) preserves \(t^4\); inversion and coordinate swaps exchange the two nonidentity cube roots. Thus permutations and fourth-root scalings act transitively on the 24 base holes. The deck involution \(w\mapsto-w\) interchanges the two rational lifts since all hole branch values are nonzero. The verifier independently generates this orbit and compares it with the complete hole set.

## Verification
Run \(`python3 verify.py`\) with a Python 3 standard library. It constructs all 25 field elements and all 651 projective base points, checks the 28 bitangents and all 44 rational branch contacts, enumerates the lifted surface counts and incidence distribution, proves set equality of the 24 projected holes with the stated coordinate condition, and verifies transitivity. It must print \(`VERIFY_OK`\). Exhaustive finite enumeration is a proof here because the claim concerns precisely \(\mathbb F_{25}\); the separate classical 28-bitangent theorem ensures no geometric exceptional curves were omitted.

## Relationship to prior work
Knecht and Reyes (arXiv:1510.04621, first posted 2015-10-15) formulate the full degree-two del Pezzo surface problem and list known full surfaces through field size 23, explicitly leaving 25 among possible field sizes. They do **not** give this Fermat surface's 48-point deficit or the exact exceptional-curve complement. Kresch and Tschinkel (2004, section 2) already record the geometric 28 Fermat bitangents and 56 exceptional curves for diagonal quartic covers: those equations and the mere splitting of curves are not new. The claimed contribution is the exact exceptional-locus rational-point coverage and intrinsic, single-orbit description of its complement at field size 25. This calculation eliminates the natural Fermat model as a full surface at that field size but does not exclude other models.

## Limitations
The result concerns one explicitly defined surface, not the existence of any full degree-two del Pezzo surface over \(\mathbb F_{25}\). The 28-bitangent theorem is used as a classical geometric input. Historical priority for the finite-field count remains conditional on unindexed earlier computations; absence of a retrieved result does not establish uniqueness or publication priority. No independent scientific audit has been performed.

## References
- A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv:1510.04621 (submitted 2015-10-15), https://arxiv.org/abs/1510.04621 .
- A. Kresch and Y. Tschinkel, *On the arithmetic of del Pezzo surfaces of degree 2*, Proc. London Math. Soc. 89 (2004), 545–569, Section 2; https://wrap.warwick.ac.uk/id/eprint/757/1/WRAP_Kresch_arithmetic_del_pezzo.pdf .
- H. Bethea and J. Brazelton, *Bitangents to symmetric quartics*, https://arxiv.org/abs/2410.09242 (symmetric complex quartic orbit background; not a finite-field coverage theorem).
