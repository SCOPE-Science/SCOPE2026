# Fixed-point branching spectra classify full zip shifts

## Finding

Let \(A\) and \(B\) be finite nonempty alphabets with \(N=|A|\ge2\), and let \(\tau:A\twoheadrightarrow B\) be any surjection. The full one-block zip shift \(F_\tau\) is defined below. For each integer \(d\ge1\), write
\[
 c_d(\tau)=\#\{p\in\operatorname{Fix}(F_\tau):\#F_\tau^{-1}(p)=d\}.
\]
Then the following conditions on two full one-block zip shifts are equivalent:

1. Their dynamical systems are topologically conjugate by an arbitrary homeomorphism of the compact phase spaces.
2. Their polynomials \(\Phi_\tau(t)=\sum_{d\ge1}c_d(\tau)t^d\) coincide.
3. The unordered multisets \(\{|\tau^{-1}(b)|:b\in B\}\) of positive fibre sizes coincide.

Indeed, the exact identity is
\[
 c_d(\tau)=d\,\#\{b\in B:|\tau^{-1}(b)|=d\}.
\]
For a fixed future-alphabet size \(N\), the number of conjugacy classes is therefore the partition number \(p(N)\); with exactly \(M\) past symbols it is the number \(p_M(N)\) of partitions of \(N\) into exactly \(M\) positive parts. The realizable polynomials \(\Phi_\tau\) are exactly the polynomials \(\sum_{d\ge1}c_dt^d\) with finitely supported nonnegative integer coefficients, \(d\mid c_d\) for each \(d\), and \(\sum_dc_d=N\).

The distinction is not detected by ordinary periodic-point counting or topological entropy: for every such \(\tau\),
\[
 \#\operatorname{Fix}(F_\tau^k)=N^k\quad(k\ge1),\qquad
 \zeta_{F_\tau}(z)=\frac{1}{1-Nz},\qquad h_{\mathrm{top}}(F_\tau)=\log N.
\]
For \(N=4\), the five possible branching polynomials are \(4t^4\), \(3t^3+t\), \(4t^2\), \(2t^2+2t\), and \(4t\), even though all five systems have the same entropy and Artin--Mazur zeta function.

## Assumptions and scope

Let \(\mathbb Z_{<0}=\{\ldots,-2,-1\}\) and \(\mathbb Z_{\ge0}=\{0,1,\ldots\}\). The phase space is the unrestricted product
\[
 X_\tau=B^{\mathbb Z_{<0}}\times A^{\mathbb Z_{\ge0}}
\]
with its compact product topology. For \(x\in X_\tau\), define \(F_\tau:X_\tau\to X_\tau\) by
\[
 (F_\tau x)_i=\begin{cases}\tau(x_0)&i=-1,\\ x_{i+1}&i\ne-1.\end{cases}
\]
The resulting point again lies in \(X_\tau\). This is the **full one-block** case, meaning that all future words are permitted and the transition symbol uses only \(x_0\). There is no uniform-fibre-size hypothesis. The theorem makes no assertion about proper sub-zip shifts, longer-block transition maps, or arbitrary finite-to-one local homeomorphisms.

Topological conjugacy means a homeomorphism \(H:X_\tau\to X_{\tau'}\) satisfying \(HF_\tau=F_{\tau'}H\). In particular, this definition does **not** assume that \(H\) respects the given coordinate alphabets or is a sliding-block relabeling.

## Proof

**1. Fibres and fixed points.** For an arbitrary \(y\in X_\tau\), each preimage \(x\) is forced by the equations \(x_i=y_{i-1}\) for all \(i\ge1\), and \(x_i=y_{i-1}\) for all \(i<0\) (the latter means \(x_{-1}=y_{-2}\), etc.). The only free coordinate is \(x_0\), which must satisfy \(\tau(x_0)=y_{-1}\). Surjectivity gives
\[
 \#F_\tau^{-1}(y)=|\tau^{-1}(y_{-1})|.
\]
For every \(a\in A\), the point \(p^a\) with \(p^a_i=a\) for \(i\ge0\) and \(p^a_i=\tau(a)\) for \(i<0\) is fixed. Conversely, \(F_\tau(p)=p\) forces the positive coordinates to be constantly \(p_0=a\), the negative coordinates to be constantly \(\tau(a)\), so these are all \(N\) fixed points. Consequently \(\#F_\tau^{-1}(p^a)=|\tau^{-1}(\tau(a))|\). Every fibre of size \(d\) contributes exactly \(d\) future letters and hence exactly \(d\) fixed points of inverse degree \(d\). This proves the displayed formula for \(c_d(\tau)\).

**2. Necessity under arbitrary conjugacy.** If \(H\) is a conjugacy, it bijects the fixed points of the two maps. Moreover, for every \(y\),
\[
 H(F_\tau^{-1}(y))=F_{\tau'}^{-1}(H(y))
\]
as an equality of finite sets, since \(H\) is bijective and intertwines the maps. Thus the number of immediate preimages of each fixed point is a topological conjugacy invariant. It follows that \(c_d(\tau)=c_d(\tau')\) for every \(d\), and division by \(d\) recovers the number of transition fibres of each size. This proves the implication from conjugacy to equality of the unordered size multisets, and shows equality of the polynomials is equivalent to equality of these multisets.

**3. Sufficiency.** Suppose the unordered multisets agree. Choose a bijection \(\beta:B\to B'\) matching fibres with equal cardinalities. For each \(b\in B\), choose an independent bijection from \(\tau^{-1}(b)\) onto \((\tau')^{-1}(\beta(b))\); their union is a bijection \(\alpha:A\to A'\) satisfying \(\tau'\circ\alpha=\beta\circ\tau\). Let \(H\) apply \(\beta\) to every negative coordinate and \(\alpha\) to every nonnegative coordinate. This is a product-coordinate homeomorphism. For coordinates other than \(-1\), \(HF_\tau=F_{\tau'}H\) follows by shifting; at \(-1\) the required equation is exactly \(\beta\tau(x_0)=\tau'\alpha(x_0)\). Therefore \(H\) is a conjugacy. This finishes the complete classification.

**4. Enumeration and possible polynomials.** A surjection on a future alphabet of size \(N\) has a finite unordered list of positive fibre sizes summing to \(N\), hence an integer partition. Every such partition can be realized by taking disjoint fibres of the prescribed sizes. The number with \(M\) parts is \(p_M(N)\), and summing over \(M\) gives \(p(N)\). The coefficient identity from step 1 proves the polynomial divisibility restrictions. Conversely, any list \(c_d\) satisfying those restrictions has \(c_d/d\) fibres of size \(d\); the total future alphabet is \(\sum_d c_d=N\), so the polynomial is realized.

**5. Entropy and ordinary periodic data.** A point fixed by \(F_\tau^k\) is uniquely determined by a positive-side \(k\)-periodic word \(a_0,\ldots,a_{k-1}\) in \(A\): extend the word periodically to nonnegative indices, and for \(i<0\) set \(x_i=\tau(a_{i\bmod k})\). This is the unique backwards symbolic completion satisfying \(F_\tau^k(x)=x\). Hence there are exactly \(N^k\) such points, and the Artin--Mazur identity follows by exponentiating \(\sum_{k\ge1}N^kz^k/k\).

For entropy, let \(\sigma\) be the bilateral full shift on \(A^{\mathbb Z}\). Define \(\pi:A^{\mathbb Z}\to X_\tau\) by \(\pi(u)_i=u_i\) for \(i\ge0\) and \(\pi(u)_i=\tau(u_i)\) for \(i<0\). This is a continuous surjective factor with \(\pi\sigma=F_\tau\pi\), proving \(h_{\rm top}(F_\tau)\le\log N\). The map from \(X_\tau\) to the one-sided full shift \(A^{\mathbb Z_{\ge0}}\) obtained by forgetting negative coordinates is likewise a continuous surjective factor and intertwines \(F_\tau\) with the unilateral shift. Thus \(h_{\rm top}(F_\tau)\ge\log N\), giving equality. Both entropy inequalities use classical monotonicity under topological factors of compact systems.

## Verification

A standalone standard-library verifier `verification.py` enumerates every onto transition map on alphabets of sizes \(2\) through \(6\), checks the fixed-point inverse-degree spectrum and the predicted partition-class count, and checks explicit coordinatewise conjugacies for representative pairs. In the recorded execution it passed \(5{,}315\) surjections, \(28\) distinct integer-partition classes, and \(23\) finite-window coordinate-conjugacy checks. Exact finite checks do not prove the infinite-product assertions; those follow from the proof above. Reproduce with `python verification.py`.

## Relationship to prior work

Lamei and Mehdipour introduced zip-shift spaces and discussed local preimages, symbolic conjugacies and examples in *Zip Shift Space* (2025), notably Section 3 and Example 4.3, which distinguishes a uniform double-cover horseshoe from a fourfold covering using zip encodings. Their *Zip Shift Encoding of m-to-1 Local Homeomorphisms* (2026), Section 3, gives the one-block zip-shift construction and Section 4 develops symbolic partitions for general local homeomorphisms. Lamei, Mehdipour and Vargas (2025), Proposition 2.22, state the standard periodic-point count; neither that count nor entropy factor monotonicity is claimed as a novelty here.

The claim above is the **complete classification under unrestricted topological conjugacy** of full one-block zip shifts with arbitrary unequal transition-fibre sizes, using an intrinsic polynomial computed from fixed points and local inverse degrees. The original examples and individual preimage descriptions are acknowledged as ingredients, but no equivalent partition-number classification was found in the primary texts inspected. This literature assessment does not establish absolute historical priority.

## Limitations

The classification covers full one-block finite-alphabet zip shifts, not proper subshifts, higher-block transition rules, or their non-symbolic realizations. The polynomial retains local inverse-degree labels: the ordinary zeta function discards this information. Originality is subject to broader historical literature in graph coverings, sliding-block systems, and local homeomorphisms; the exact same statement might be known in different language.

## References

1. S. Lamei and P. Mehdipour, *Zip Shift Space* (2025), arXiv:2502.11272, https://ar5iv.labs.arxiv.org/html/2502.11272. Sections 2--5, especially Section 3 and Example 4.3.
2. P. Mehdipour and S. Lamei, *Zip Shift Encoding of m-to-1 Local Homeomorphisms*, Advances in Pure and Applied Mathematics 17(2), 20--29 (2026), DOI:10.21494/ISTE.OP.2026.1442, https://www.openscience.fr/IMG/pdf/iste_apam26v17n2_2.pdf. Sections 3--4.
3. S. Lamei, P. Mehdipour and W. Vargas, *S-Expansiveness and Zip Shift Maps in Symbolic Dynamics* (2025), arXiv:2510.12980. Section 2.1 and Proposition 2.22.
