# The general syzygy-bundle hypersurface has automorphism group \(S_4\)
## Finding
Let \(W\subset H^0(\mathbf P^2_{{\mathbf C}},\mathcal O_{{\mathbf P^2}}(2))\) be a general basepoint-free four-dimensional subspace. Write \(M_W\) for the kernel of the evaluation map
\[
W\otimes\mathcal O_{{\mathbf P^2}}\longrightarrow\mathcal O_{{\mathbf P^2}}(2),
\]
and set
\[
X_W=\mathbf P_{{\mathbf P^2}}(M_W)\subset\mathbf P^2\times\mathbf P^3.
\]
Then
\[
\operatorname{{Aut}}(X_W)\cong S_4.
\]
In particular, the generic finite automorphism group in this exceptional bidegree-\((2,1)\) family has order \(24\).

## Assumptions and scope
The ground field is \(\mathbf C\). The subspace \(W\) is assumed basepoint-free, as in the syzygy-bundle construction of Bunnett--Namanya. The word "general" is used only to ensure that the annihilator pencil \(\mathbf P(W^\perp)\) has four distinct base points in general position. Equivalently, the argument applies to every \(W\) in that open locus. No statement is made for degenerate pencils; the cited source exhibits special choices with positive-dimensional stabilizer.

## Proof
Bunnett--Namanya identify the associated smooth hypersurface with the projectivized syzygy bundle and prove, in their exceptional \(\mathbf P^2\times\mathbf P^3\) analysis, that
\[
\operatorname{{Aut}}(X_W)\cong \operatorname{{Stab}}_{{\operatorname{{PGL}}_3}}(W).
\]
Passing to the annihilator identifies the same stabilizer with the stabilizer of the pencil \(\mathbf P(W^\perp)\) of plane conics. For general \(W\), the source further records that this pencil has four distinct base points in general position.

Let the base locus be \(Z=\{{p_1,p_2,p_3,p_4}\}\). Four points in general position impose four independent linear conditions on the six-dimensional vector space \(H^0(\mathbf P^2,\mathcal O(2))\). Therefore the vector space of conics through \(Z\) has dimension \(2\), so its projectivization is exactly the given pencil. It follows in both directions that
\[
\operatorname{{Stab}}_{{\operatorname{{PGL}}_3}}\bigl(\mathbf P(W^\perp)\bigr)
=
\operatorname{{Stab}}_{{\operatorname{{PGL}}_3}}(Z).
\]
Indeed, a transformation preserving the pencil preserves its scheme-theoretic base locus; conversely, a transformation preserving \(Z\) preserves the full two-dimensional space of conics through \(Z\).

The ordered tuple \((p_1,p_2,p_3,p_4)\) is a projective frame of \(\mathbf P^2\). Projective linear transformations act simply transitively on ordered projective frames. Hence each of the \(24\) permutations of \(Z\) is induced by a unique element of \(\operatorname{{PGL}}_3\), and an element fixing all four points is the identity. Thus
\[
\operatorname{{Stab}}_{{\operatorname{{PGL}}_3}}(Z)\cong S_4.
\]
Combining the displayed identifications proves the claim.

## Verification
A standalone exact-symbolic check is included as `verify_frame_stabilizer.py`. It normalizes the four points to
\[
(1:0:0),\ (0:1:0),\ (0:0:1),\ (1:1:1),
\]
constructs the unique projective matrix for each of the \(24\) permutations, verifies that the matrices are projectively distinct, and checks that each preserves the two-dimensional pencil of conics through the frame. Its recorded output ends in `VERIFY_OK`. This finite computation is a reproducibility check of the projective-frame step, not a substitute for the proof above.

## Relationship to prior work
Bunnett--Namanya prove the key geometric reduction \(\operatorname{{Aut}}(X_W)\cong\operatorname{{Stab}}_{{\operatorname{{PGL}}_3}}(W)\) and show that, for general \(W\), the annihilator pencil has four distinct base points in general position; they conclude finiteness. Their full text does not state the resulting exact group \(S_4\) or its order \(24\). The present observation closes that last stabilizer computation by the projective-frame argument. Searches for the exact syzygy-bundle statement, for equivalent conic-pencil formulations, and for broader automorphism results did not locate a published statement implying the displayed isomorphism for this family; detailed comparisons are recorded in `AUDIT.json`.

## Limitations
The conclusion concerns the general four-point locus in characteristic zero. It does not classify automorphism groups on the discriminant where base points collide, become nonreduced, or cease to be in general position. It also does not assert that every deformation or compactification of the family has the same stabilizer. The computational check treats one normalized projective frame; projective equivalence of all frames is used in the proof to obtain the general statement.

## References
Dominic Bunnett and Caroline Namanya, *Finite automorphism groups of hypersurfaces via Bott vanishing*, arXiv:2609.38572v1, especially the discussion of syzygy bundles in \(\mathbf P^2\times\mathbf P^3\), first public 2026-09-29.
