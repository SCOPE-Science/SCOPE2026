# Relative-trace collapse of a Gold defining-set code family
## Finding
Let \(m=2e\), \(F=\mathbb F_{{2^{{2e}}}}\), and \(K=\mathbb F_{{2^e}}\). In the Gold-type construction of Xiang and Song, define \(N=N_{{F/K}}\), \(c_i=\operatorname{{Tr}}_{{F/K}}(a_i)=a_i+a_i^{{2^e}}\), and
\[
C=\langle c_1,c_2\rangle_{{\mathbb F_2}}\subseteq K,
\qquad r=\dim_{{\mathbb F_2}} C.
\]
Then the defining set has the exact norm-fiber description
\[
D=\{{x\in F^\times:N(x)\in C^\perp\}},
\qquad
C^\perp=\{{y\in K:\operatorname{{Tr}}_{{K/\mathbb F_2}}(cy)=0\text{{ for every }}c\in C\}}.
\]
Hence
\[
|D|=(2^{{e-r}}-1)(2^e+1).
\]
If \(C'=sC\) for some \(s\in K^\times\), the two trace codes are permutation-equivalent. In addition, the norm-one group \(U=\ker N\) is a cyclic subgroup of the coordinate automorphism group of order \(2^e+1\) and acts freely on \(D\).

For the three parameter regimes grouped together in Xiang--Song Theorem 3.5, \(r=1\). Therefore, for each fixed even \(m\) in that theorem, all of those parameter choices produce a single permutation-equivalence class. Its coordinate set is a disjoint union of exactly \(2^{{e-1}}-1\) free orbits of \(U\), each of size \(2^e+1\).

## Assumptions and scope
The statement concerns the binary defining-set code
\[
\mathcal C_D=\{{(\operatorname{{Tr}}_{{F/\mathbb F_2}}(bd))_{{d\in D}}:b\in F\}},
\]
with
\[
D=\{{x\in F^\times:\operatorname{{Tr}}_{{F/\mathbb F_2}}(a_1x^{{2^e+1}})=\operatorname{{Tr}}_{{F/\mathbb F_2}}(a_2x^{{2^e+1}})=0\}}.
\]
This is the construction in Xiang--Song, with \(m=2e\). The permutation-equivalence conclusion for Theorem 3.5 uses its hypotheses \(m\ge 6\), \(a_1,a_2\notin\mathbb F_2\), and \(a_1\ne a_2\). The structural norm-fiber identity itself is valid whenever the displayed construction is defined.

## Proof
Because \(x^{{2^e+1}}=N_{{F/K}}(x)\in K\), transitivity of trace gives, for every \(a,x\in F\),
\[
\operatorname{{Tr}}_{{F/\mathbb F_2}}(aN(x))
=\operatorname{{Tr}}_{{K/\mathbb F_2}}\bigl(\operatorname{{Tr}}_{{F/K}}(a)N(x)\bigr).
\]
Thus the two defining equations depend on \(a_1,a_2\) only through \(c_1,c_2\), and they say exactly that \(N(x)\in C^\perp\). This proves the norm-fiber description.

The norm map \(N:F^\times\to K^\times\) is surjective and every nonzero norm fiber has size
\[
|\ker N|=\frac{2^{{2e}}-1}{2^e-1}=2^e+1.
\]
Since \(C^\perp\) has \(2^{{e-r}}\) elements and only its nonzero elements have preimages in \(F^\times\),
\[
|D|=(2^{{e-r}}-1)(2^e+1).
\]

Now let \(C'=sC\) with \(s\in K^\times\). Then \(C'^\perp=s^{{-1}}C^\perp\). Choose \(t\in F^\times\) with \(N(t)=s^{{-1}}\). Multiplication \(x\mapsto tx\) bijects \(D_C\) onto \(D_{{C'}}\). Under this coordinate bijection,
\[
\operatorname{{Tr}}_{{F/\mathbb F_2}}(bx)
=\operatorname{{Tr}}_{{F/\mathbb F_2}}((bt^{{-1}})(tx)),
\]
so, as \(b\) ranges over \(F\), the two codes are permutation-equivalent.

For \(u\in U=\ker N\), multiplication by \(u\) preserves every norm fiber and therefore preserves \(D\). The same trace reparameterization shows that it induces a coordinate automorphism of the code. Since \(F^\times\) is cyclic, \(U\) is cyclic of order \(2^e+1\). Its action on \(F^\times\), and hence on \(D\), is free.

Finally, the kernel of \(a\mapsto a+a^{{2^e}}\) is exactly \(K\). In the first two cases of Theorem 3.5 one of \(c_1,c_2\) is zero and the other is nonzero. In the third case, both are nonzero and \(a_1+a_2\in K\), so \(c_1+c_2=0\) and hence \(c_1=c_2\). Thus \(r=1\) in every case. All one-dimensional \(\mathbb F_2\)-subspaces of \(K\) are scalar multiples of one another, proving the stated collapse to one permutation-equivalence class. The orbit count follows from \(|D|=(2^{{e-1}}-1)(2^e+1)\).

## Verification
A standalone verifier checks the smallest parameter size of Theorem 3.5, \(m=6\), using exact arithmetic in \(\mathbb F_{{64}}\). It verifies the trace-transitivity identity for every pair of field elements, norm surjectivity, the norm-one subgroup order, every one of the \(1064\) ordered parameter pairs satisfying the three Theorem 3.5 regimes, the explicit coordinate normalization to one canonical defining set, and invariance under the full norm-one subgroup.

For the canonical \(m=6\) representative, the verifier obtains length \(27\) and weight enumerator
\[
1+36z^{{12}}+27z^{{16}},
\]
matching Table 2 of the source. Running `python3 verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Xiang and Song define the Gold-type code and determine its lengths and weight distributions by exponential-sum calculations. Their Theorem 3.5 groups three parameter regimes and gives the same two-weight distribution, but the inspected full text does not identify the relative-trace/norm reduction, does not state permutation equivalence among those regimes, and does not describe the norm-one coordinate automorphisms. The source explicitly presents the parameters as varying with the ranges of \(a_1\) and \(a_2\); the result here separates genuine variation from parameter redundancy at the code-equivalence level.

The generic defining-set literature records that reordering a fixed defining set gives a permutation-equivalent code. That general observation does not imply the present statement: the key step here is that different source parameter pairs define norm preimages attached to scalar-equivalent relative-trace subspaces, and scalar equivalence is realized by norm-surjective multiplication in \(F\).

## Limitations
The result proves a specific coordinate-automorphism subgroup, not the full automorphism group. It proves that scalar-equivalent relative-trace constraint subspaces give permutation-equivalent codes; it does not prove the converse for higher-dimensional constraint subspaces. In particular, no exact classification of the rank-two family in Xiang--Song Theorem 3.6 is claimed. The finite verifier checks \(m=6\) exhaustively, while the all-even-
\(m\) statement rests on the algebraic proof above rather than on finite enumeration.

## References
1. C. Xiang and Y. Song, “Binary self-orthogonal codes with few weights,” *Advances in Mathematics of Communications* 23 (2026), 146–156. DOI: 10.3934/amc.2026017. Early access: 2026-02-09.
2. R. Lidl and H. Niederreiter, *Finite Fields*, Cambridge University Press, 1997. Standard facts on trace and norm in finite fields.
