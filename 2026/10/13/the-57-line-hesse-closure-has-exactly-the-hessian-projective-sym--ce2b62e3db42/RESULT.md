# The \(57\)-line Hesse closure has exactly the Hessian projective symmetry group
## Finding
Let \(\mathcal H\subset\mathbb P^2_{\mathbb C}\) be the classical Hesse arrangement of twelve inflection lines and let
\[
\mathcal H_{57}=\Lambda_{2,2}(\mathcal H),
\]
where \(\Lambda_{2,2}\) takes the union of all lines containing at least two points of multiplicity at least two. For the fifty-seven-line arrangement introduced by Pokora and Roulleau,
\[
\operatorname{Stab}_{\operatorname{PGL}_3(\mathbb C)}(\mathcal H_{57})
=G_{216}
\cong (C_3)^2\rtimes\operatorname{SL}(2,3).
\]
In particular, its full projective stabilizer has order \(216\).

There is an intrinsic recovery rule for the original Hesse arrangement. The singular locus of \(\mathcal H_{57}\) contains exactly twenty-one points of multiplicity eight. Counting, for each line of \(\mathcal H_{57}\), how many of these eightfold points lie on it gives
\[
12\text{ lines with }5,
\qquad 9\text{ lines with }4,
\qquad 36\text{ lines with }2.
\]
The twelve lines in the first class are exactly \(\mathcal H\).

## Assumptions and scope
The ground field is \(\mathbb C\). The arrangement \(\mathcal H_{57}\) is the arrangement defined by the fifty-seven explicit linear forms in the proof of Theorem A of Pokora--Roulleau, with a primitive cube root \(\varepsilon\) satisfying \(\varepsilon^2+\varepsilon+1=0\). Projective stabilizer means the subgroup of \(\operatorname{PGL}_3(\mathbb C)\) carrying the reduced union of the fifty-seven lines to itself.

The claim concerns projective automorphisms of the embedded arrangement. It does not claim that every abstract automorphism of the incidence lattice is projectively realizable.

## Proof
Pokora--Roulleau define \(\mathcal H_{57}=\Lambda_{2,2}(\mathcal H)\) and give the complete list of its fifty-seven lines. Their Theorem A records the singularity counts
\[
n_2=252,\qquad n_3=108,\qquad n_4=72,\qquad n_8=21.
\]
Starting from the printed fifty-seven linear forms, exact arithmetic in \(\mathbb Q(\varepsilon)\) reproduces all pairwise intersections and these multiplicities. It further computes the incidence of each line with the twenty-one eightfold points. The resulting line profile is exactly
\[
5^{\times12},\qquad 4^{\times9},\qquad 2^{\times36}.
\]

The same exact computation identifies the twelve lines in the \(5\)-class with
\[
x=0,\quad y=0,\quad z=0,
\]
and the nine lines
\[
x+\varepsilon^i y+\varepsilon^j z=0
\qquad (i,j\in\mathbb Z/3\mathbb Z),
\]
which are precisely the classical Hesse arrangement \(\mathcal H\). Thus \(\mathcal H\) is canonically recoverable from the embedded incidence geometry of \(\mathcal H_{57}\): it is the set of lines containing five eightfold points.

Any projective transformation preserving \(\mathcal H_{57}\) preserves intersection multiplicities, hence preserves the set of its twenty-one eightfold points and therefore the distinguished set of twelve lines just recovered. Consequently
\[
\operatorname{Stab}(\mathcal H_{57})\subseteq\operatorname{Stab}(\mathcal H).
\]
The twelve Hesse lines contain the nine quadruple points of the Hesse configuration, so their projective stabilizer is the classical Hessian group \(G_{216}\). Artebani--Dolgachev identify this group as
\[
G_{216}\cong (C_3)^2\rtimes\operatorname{SL}(2,3)
\]
of order \(216\).

For the reverse inclusion, the operator \(\Lambda_{2,2}\) is defined only from incidence and multiplicity. Hence it is projectively covariant: for every projectivity \(g\),
\[
g\bigl(\Lambda_{2,2}(\mathcal L)\bigr)=\Lambda_{2,2}(g\mathcal L).
\]
Every element of \(G_{216}=\operatorname{Stab}(\mathcal H)\) therefore preserves \(\Lambda_{2,2}(\mathcal H)=\mathcal H_{57}\). This proves the reverse inclusion and hence equality.

## Verification
The accompanying `verify.py` works exactly over \(\mathbb Q(\varepsilon)\), represented as pairs of rational numbers modulo \(\varepsilon^2+\varepsilon+1=0\). It checks all \(\binom{57}{2}\) line intersections, verifies that the multiplicity census is \((252,108,72,21)\) for multiplicities \((2,3,4,8)\), verifies that all line-pair incidences are exhausted, computes the \(12+9+36\) eightfold-point incidence profile, and checks set equality between the twelve five-point lines and the standard twelve Hesse lines.

A fresh replay with Python 3.13.5 and only the standard library returned:

`VERIFY_OK lines=57 singularities=n2:252,n3:108,n4:72,n8:21 maxpoint_profile=12x5+9x4+36x2 recovered_hesse=exact`

The computation establishes the intrinsic recovery lemma. The group-theoretic identification of the stabilizer of the recovered Hesse configuration uses the published Hessian-group theorem rather than a finite numerical search.

## Relationship to prior work
Pokora--Roulleau construct \(\mathcal H_{57}\), list its fifty-seven lines, prove rigidity and freeness, and give its singularity counts. Their paper motivates the use of point-line operators partly by arrangements with substantial symmetry, but it does not state the full projective automorphism group of \(\mathcal H_{57}\), nor the \(12+9+36\) profile by eightfold-point incidence.

Artebani--Dolgachev describe the classical Hessian group \(G_{216}\), its order and semidirect-product structure, and the invariance of the twelve Hesse inflection lines. Combining that classical result with the new intrinsic recovery of \(\mathcal H\) inside \(\mathcal H_{57}\) gives the exact stabilizer: the point-line closure introduces no accidental projective symmetries.

## Limitations
The result is over \(\mathbb C\) and concerns the explicit Pokora--Roulleau realization. It does not compute the full abstract automorphism group of the incidence lattice and does not address reductions in characteristics \(2\) or \(3\), where the displayed cyclotomic realization degenerates or changes. The literature search did not find a prior statement of this exact stabilizer or the intrinsic recovery rule, but older configuration literature using different terminology remains a residual originality risk.

## References
P. Pokora and X. Roulleau, “Construction of free arrangements using point-line operators,” arXiv:2403.20024v1, first posted 29 March 2024; Theorem A and its proof.

M. Artebani and I. Dolgachev, “The Hesse pencil of plane cubic curves,” L'Enseignement Mathématique 55 (2009), 235–273, DOI 10.4171/LEM/55-3-3; especially Proposition 4.1 and the discussion of the twelve inflection lines.
