# Trace stratifies commutants in the five-dimensional Nagy–Zhou semifields
## Finding
Let \(q\equiv1\pmod 3\) be a prime power, let \(K=\mathbb F_q\), let \(F=\mathbb F_{q^5}\), choose \(w\in K\) with \(w^2-w+1=0\), and let \(s\) be a unit modulo \(5\). Put \(\sigma(x)=x^{q^s}\), and equip \(F\) with the Nagy–Zhou multiplication
\[
x*_{w,s}y=x^{\sigma}y^{\sigma^2}+x^{\sigma}y^{\sigma^{-1}}+x^{\sigma^{-2}}y^{\sigma^{-1}}+w\bigl(x^{\sigma^2}y^{\sigma}+x^{\sigma^{-1}}y^{\sigma}+x^{\sigma^{-1}}y^{\sigma^{-2}}\bigr).
\]
For \(x\in F\), define the \(K\)-linear commutator map \(C_x:F\to F\) by \(C_x(y)=x*_{w,s}y-y*_{w,s}x\). Then
\[
\operatorname{rank}_K C_x=
\begin{cases}
0,&x=0,\\
2,&x\ne0\text{ and }\operatorname{Tr}_{F/K}(x)=0,\\
4,&\operatorname{Tr}_{F/K}(x)\ne0.
\end{cases}
\]
Equivalently, the commutant \(\mathcal C(x)=\{y\in F:x*_{w,s}y=y*_{w,s}x\}\) has \(K\)-dimension \(5,3,1\) in the three cases above. Consequently the exact number of ordered commuting pairs is
\[
q^5+(q^4-1)q^3+(q^5-q^4)q=q^7+q^6-q^3,
\]
and the commuting probability of the displayed multiplication is
\[
q^{-3}+q^{-4}-q^{-7}.
\]
## Assumptions and scope
The statement concerns the native presemifield multiplication \(*_{w,s}\) in extension degree \(5\). It holds uniformly for every admissible prime power \(q\), both odd and even characteristic, because \(q\equiv1\pmod3\) only excludes characteristic \(3\). The parameter \(s\) may be any generator of \(\operatorname{Gal}(F/K)\), and either root \(w\) of \(w^2-w+1\) is allowed. The commuting probability is a property of this displayed multiplication; it is not asserted to be invariant under arbitrary isotopy.
## Proof
Write \(X_i=x^{\sigma^i}\) and \(Y_i=y^{\sigma^i}\), with indices modulo \(5\). Subtracting the multiplication with the two inputs exchanged and using \(w^{-1}=1-w\) shows that the scalar \(1-w\ne0\) factors out. After removing this harmless scalar, the split matrix of \(C_x\) is the alternating matrix
\[
M(X)=\begin{pmatrix}
0&-(X_2+X_4)&X_1&-X_4&X_1+X_3\\
X_2+X_4&0&-(X_0+X_3)&X_2&-X_0\\
-X_1&X_0+X_3&0&-(X_1+X_4)&X_3\\
X_4&-X_2&X_1+X_4&0&-(X_0+X_2)\\
-(X_1+X_3)&X_0&-X_3&X_0+X_2&0
\end{pmatrix}.
\]
Set \(S=X_0+X_1+X_2+X_3+X_4\). Direct polynomial expansion gives
\[
\det M(X)=0
\]
and, for every \(0\le r,c<5\),
\[
\det M(X)_{\widehat r,\widehat c}=(-1)^{r+c}X_rX_cS^2,
\]
where the hats mean that row \(r\) and column \(c\) are deleted. The supplied symbolic checker verifies all twenty-five identities over \(\mathbb Z[X_0,\ldots,X_4]\), so the identities remain valid in every characteristic.

For an actual nonzero field element \(x\), every conjugate \(X_i\) is nonzero, and because \(\sigma\) generates \(\operatorname{Gal}(F/K)\),
\[
S=\sum_{i=0}^4x^{\sigma^i}=\operatorname{Tr}_{F/K}(x).
\]
The Moore change between ordinary coordinates and the conjugate coordinates is invertible, so it preserves the \(K\)-rank of the linear map.

If \(\operatorname{Tr}_{F/K}(x)\ne0\), the diagonal cofactor \(X_r^2S^2\) is nonzero, giving rank at least \(4\); the zero determinant gives rank exactly \(4\). If \(x\ne0\) and \(\operatorname{Tr}_{F/K}(x)=0\), every \(4\times4\) minor vanishes, so the rank is at most \(3\). An alternating matrix has even rank over every field, including characteristic \(2\), hence the rank is at most \(2\). The entry \(M_{0,2}=X_1\) is nonzero, so the rank is exactly \(2\). Finally \(C_0=0\).

The trace map \(F\to K\) is a nonzero \(K\)-linear functional, so its kernel has \(q^4\) elements. Summing the commutant sizes \(q^5\), \(q^3\), and \(q\) over the three strata gives the stated commuting-pair count and probability.
## Verification
Running `python verify_commutator.py` from the supplied package checks the alternating matrix, its zero determinant, and all twenty-five cofactor identities symbolically. The captured output in `verification_output.txt` is `VERIFY_OK`. The proof then uses only invertibility of the Moore coordinate change, nonvanishing of field conjugates of a nonzero element, the standard even-rank property of alternating forms, and the size of the trace-zero hyperplane.
## Relationship to prior work
Nagy and Zhou introduced the family in arXiv:2609.32651v1 (26 September 2026). Their equations (20)–(25) give the parameters and multiplication, Theorem 3.1 proves the division property through multiplication determinants, Theorem 5.1 and Corollary 5.2 determine nuclei and centre, and Theorem 5.4 with Corollary 5.7 determines isotopies and proves that the Knuth orbit has no commutative isotope. The full text was searched for “commutator”, “commuting”, and “centralizer”; none occurs. The present claim instead determines the rank of the difference of left and right multiplication by each element and exactly counts commuting pairs. Neither the division determinant nor the no-commutative-isotope statement implies this elementwise rank stratification.

A separate literature search for finite-semifield centralizers, commuting pairs, and commuting probability found work connecting presemifields with class-two groups, but that group-theoretic commutator construction concerns an associated group rather than the equation \(x*y=y*x\) inside this multiplication. No source located in the searches states the trace-stratified ranks or the formula \(q^{-3}+q^{-4}-q^{-7}\).
## Limitations
The theorem is proved only for extension degree \(5\); the same cofactor factorization has not been established here for the higher odd dimensions in the Nagy–Zhou family. It concerns the displayed presemifield multiplication, not all isotopes. Literature search cannot prove absolute novelty, and specialized classification tables or terminology not indexed by the searched sources remain a residual originality risk.
## References
1. G. P. Nagy and Y. Zhou, “Semifields in prime dimensions and counterexamples to Kaplansky’s conjecture,” arXiv:2609.32651v1, first posted 26 September 2026, https://arxiv.org/abs/2609.32651v1.
2. M. Biliotti, V. Jha, and N. Johnson, “A note on finite semifields and certain p-groups of class 2,” Discrete Mathematics 267 (2003), DOI: 10.1016/j.disc.2003.04.002. This is used only as a comparison point for group commutators associated with presemifields.
