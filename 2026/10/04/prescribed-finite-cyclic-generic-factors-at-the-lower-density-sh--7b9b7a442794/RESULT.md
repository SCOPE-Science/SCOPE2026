# Prescribed finite cyclic generic factors at the lower-density shadowing endpoint

## Finding
For every integer \(m\ge 2\), start with the nontrivial proximal mixing subshift \((Y,g)\) used by Wu, Wei and Zhang, with fixed point \(p\) and a \(g\)-invariant Borel probability measure \(\mu\) of full support. Put
\[
X_m=(Y\times\mathbb Z/m\mathbb Z)/\sim,
\]
where all points \((p,e)\) are identified to one point \(p_*\) and every other equivalence class is a singleton. If \(q\) is the quotient map, define
\[
f_m(q(y,e))=q(g(y),e+1).
\]
Then \((X_m,f_m)\) is an E-system with \(\mathscr M_0\)-shadowing. Its maximal equicontinuous generic factor is the cyclic rotation
\[
R_m(e)=e+1\quad\text{on}\quad C_m=\mathbb Z/m\mathbb Z,
\]
and \((C_m,R_m)\) is not an ordinary topological factor of \((X_m,f_m)\). For every integer \(r\ge1\),
\[
f_m^r\text{ is topologically transitive}\quad\Longleftrightarrow\quad\gcd(r,m)=1.
\]
Consequently \((X_m,f_m)\) is not weakly mixing and has no \(\mathscr M_\alpha\)-shadowing for any \(\alpha\in(0,1)\).

## Assumptions and scope
The base system is the proximal mixing subshift \((Y,g)\) recalled in Example 4.1 of Wu--Wei--Zhang. Its fixed point is \(p=0^\infty\), and Kwietniak--Łącka--Oprocha prove that this subshift is mixing and supports an invariant probability measure of full support. The quotient relation above is closed, so \(X_m\) is compact and metrizable. The statement concerns every finite integer \(m\ge2\) and every positive integer power \(r\).

A generic factor is used in the sense of Huang--Ye: the factor map is defined continuously on the set of transitive points. The maximality assertion is only in this generic category. It deliberately does not assert that the sheet-label map extends to an ordinary continuous factor on all of \(X_m\).

## Proof
Write \(X_e=q(Y\times\{e})\). The point \(p_*\) is fixed because \(g(p)=p\). The map \(f_m\) is well defined and continuous, and
\[
f_m^m(q(y,e))=q(g^m(y),e).
\]
Because \(g\) is mixing, it is surjective, hence so is \(f_m\).

For any \(x=q(y,e)\), proximality of \(y\) to \(p\) gives a sequence \(n_j\to\infty\) with \(g^{n_j}(y)\to p\). Passing to a subsequence on which \(e+n_j\pmod m\) is constant gives \(f_m^{n_j}(x)\to p_*\). Thus every point of \(X_m\) is proximal to the fixed point \(p_*\). Lemma 4.3 of Wu--Wei--Zhang therefore gives the \(\mathscr M_0\)-shadowing property.

Define
\[
\nu_m(A)=\frac1m\sum_{e\in\mathbb Z/m\mathbb Z}\mu\bigl(\{y:q(y,e)\in A\}\bigr).
\]
The \(g\)-invariance of \(\mu\) and the cyclic sheet shift imply that \(\nu_m\) is \(f_m\)-invariant, and full support of \(\mu\) gives \(\operatorname{supp}\nu_m=X_m\).

We next prove the power-transitivity law. Since \(Y\) is nontrivial and mixing, \(p\) is not isolated. Hence every nonempty open subset of \(X_m\) contains a set of the form \(q(U'\times\{e_0})\), where \(U'\subseteq Y\setminus\{p}\) is nonempty and open. Given two nonempty open sets, choose such pieces \(q(U'\times\{e_0})\) and \(q(V'\times\{e_1})\). If \(\gcd(r,m)=1\), there are arbitrarily large integers \(n\) satisfying
\[
rn\equiv e_1-e_0\pmod m.
\]
Mixing gives \(g^{rn}(U')\cap V'\ne\varnothing\) for every sufficiently large such \(n\), so \((f_m^r)^n(U)\cap V\ne\varnothing\). Conversely, if \(d=\gcd(r,m)>1\), the residue of the sheet index modulo \(d\) is preserved by \(f_m^r\) away from \(p_*\). Two sheet-open sets with incompatible residues can never meet under any iterate, so \(f_m^r\) is not transitive.

In particular \(f_m\) itself is transitive, so together with the full-support invariant measure it is an E-system. The same sheet arithmetic directly shows non-weak-mixing: for disjoint sheet-open sets \(U_0\subset X_0\setminus\{p_*}\) and \(U_1\subset X_1\setminus\{p_*}\), a simultaneous hit from \(U_0\times U_0\) to \(U_0\times U_1\) would require the same time to be congruent to both \(0\) and \(1\) modulo \(m\), which is impossible.

Now let \(T=\operatorname{Tran}(X_m,f_m)\). Since \(p_*\notin T\), the sheet label
\[
\pi_m(q(y,e))=e\qquad(q(y,e)\in T)
\]
is continuous on \(T\), intertwines \(f_m\) with \(R_m\), and is onto because the image of a transitive orbit is dense in the finite cycle. Thus \(C_m\) is an equicontinuous generic factor.

To prove maximality, let \(\pi:T\to Z\) be any equicontinuous generic homomorphism to a transitive equicontinuous system \((Z,h)\). For each sheet put \(T_e=T\cap X_e\). A point of \(T_e\) is transitive for \(f_m^m|_{X_e}\), and conversely a point transitive for this return map is transitive for \(f_m\). Hence \(T_e=\operatorname{Tran}(X_e,f_m^m)\). The return system is conjugate to \((Y,g^m)\), so it is mixing, has a full-support invariant measure, and is therefore a weakly mixing E-system.

Let \(Z_e=\overline{\pi(T_e)}\). The restriction of \(\pi\) is a generic homomorphism from \((X_e,f_m^m)\) to the transitive equicontinuous return system \((Z_e,h^m)\). By the Huang--Ye characterization recalled as Lemmas 2.1--2.2 in Wu--Wei--Zhang, a weakly mixing E-system has no nontrivial equicontinuous generic factor. Therefore every \(Z_e\) is a singleton, say \(Z_e=\{z_e}\). Equivariance gives \(h(z_e)=z_{e+1}\). Since \(z_0\) is transitive in \(Z\), \(Z\) is precisely its finite orbit; its period divides \(m\). Thus every equicontinuous generic factor is a quotient of \(C_m\), proving that \(C_m\) is the maximal equicontinuous generic factor.

Finally, \(C_m\) cannot be an ordinary topological factor: if a continuous factor map \(\Phi:X_m\to C_m\) existed, the fixed point would satisfy \(\Phi(p_*)=R_m(\Phi(p_*))\), impossible because \(R_m\) has no fixed point for \(m\ge2\). Since the system is an E-system but is not weakly mixing, Theorem 4.1 of Wu--Wei--Zhang rules out \(\mathscr M_\alpha\)-shadowing for every \(\alpha\in(0,1)\).

## Verification
The quotient construction was checked for closedness of the equivalence relation, well-definedness of \(f_m\), and preservation of compact metrizability. The proof uses only exact congruence arithmetic and qualitative mixing/proximality facts; no numerical or finite-experiment inference is used. The key maximality step was checked sheet by sheet using the return system \(f_m^m|_{X_e}\cong g^m\), which is mixing and carries the restricted full-support invariant measure. The distinction between generic and ordinary factors is essential and is explicitly enforced by the fixed-point obstruction.

## Relationship to prior work
Wu--Wei--Zhang prove that an E-system with \(\mathscr M_\alpha\)-shadowing is weakly mixing for \(\alpha\in(0,1)\), and their Example 4.1 constructs the two-sheet case at \(\alpha=0\). Their example establishes an endpoint counterexample to weak mixing but does not state the arbitrary \(m\)-sheet family, identify its maximal equicontinuous generic factor, classify exactly which powers are transitive, or separate that generic factor from ordinary topological factors.

Kwietniak--Łącka--Oprocha provide the proximal mixing subshift with a full-support invariant measure used as the base. Huang--Ye develop generic factors and the weak-scattering characterization; Keller proves existence and structural properties of maximal equicontinuous generic factors for E-systems. These results supply the framework but do not imply the explicit finite-cyclic classification above without the sheet-return argument.

## Limitations
The construction is specialized to finite cyclic sheet permutations over the indicated proximal mixing base. It does not classify all endpoint \(\mathscr M_0\)-shadowing E-systems, all possible maximal equicontinuous generic factors, or noncyclic finite generic factors. The maximal factor is generic only; an ordinary factor is excluded. The positive-parameter nonexistence conclusion uses the E-system theorem of Wu--Wei--Zhang rather than a direct obstruction to tracing. Because the construction is elementary once the two-sheet example and generic-factor machinery are combined, there remains a residual possibility that an equivalent arbitrary-cycle observation exists as unindexed folklore.

## References
1. X. Wu, J. Wei and X. Zhang, “Weak mixing for dynamical systems with \(\mathscr M_\alpha\)-shadowing,” arXiv:2609.31724v1, 22 September 2026.
2. D. Kwietniak, M. Łącka and P. Oprocha, “Generic points for dynamical systems with average shadowing,” Monatshefte für Mathematik 183 (2017), 625–648, DOI 10.1007/s00605-016-1002-1.
3. W. Huang and X. Ye, “Generic eigenvalues, generic factors and weak disjointness,” Contemporary Mathematics 567 (2012), 119–142.
4. G. Keller, “Maximal equicontinuous generic factors and weak model sets,” Discrete and Continuous Dynamical Systems 40 (2020), 6855–6875, DOI 10.3934/dcds.2020132.
