# Cyclic divisibility and reversal-blind rank spectra of finite deterministic modal frames
## Finding

Let \(\mathbf C(\mathbf s)\) be the finite deterministic Kripke frame built from a directed cycle of \(c\geq1\) worlds \(v_i\) and \(s_i\geq0\) additional worlds \(w_{i,j}\), each with the unique successor \(v_i\). The cycle successors are \(v_i\mapsto v_{i+1}\), with subscripts modulo \(c\). Write \(\mathbf s=(s_0,\dots,s_{c-1})\). A finite Boolean modal algebra is attached by \(\mathcal A(\mathbf s)=(\mathcal P(\mathbf C(\mathbf s)),\Box)\), where \(\Box U\) is the inverse image of \(U\) under the successor function.

For integers \(p,q\geq0\), set
\[
Q_{p,q}(u)=\sum_{j=0}^{q}\binom qj\left(\sum_{b=0}^{j}(-1)^{j-b}\binom jb(b+1)^p\right)u^j.
\]

**Complete inter-frame classification.** Let \(\mathbf C(\mathbf t)\) have cycle length \(d\geq1\), where \(\mathbf t=(t_0,\dots,t_{d-1})\). A bounded Kripke-frame morphism from \(\mathbf C(\mathbf s)\) to \(\mathbf C(\mathbf t)\) exists if and only if \(d\mid c\). When this holds, put
\[
P_j^{(a)}=\sum_{\substack{0\leq i<c\\ i+a\equiv j\pmod d}}s_i
\qquad(0\leq j<d,\;0\leq a<d).
\]
The polynomial enumerating *all* bounded frame morphisms by the number of additional target leaves in their image is exactly
\[
\boxed{\mathsf H_{\mathbf s,\mathbf t}(u)=
\sum_{a=0}^{d-1}\prod_{j=0}^{d-1}Q_{P_j^{(a)},t_j}(u).}
\]
For \(d\nmid c\), define \(\mathsf H_{\mathbf s,\mathbf t}(u)=0\). Its coefficient of \(u^k\) is the number of such maps with image cardinality \(d+k\). Under finite modal-algebra duality the corresponding homomorphisms \(\mathcal A(\mathbf t)\to\mathcal A(\mathbf s)\) have image algebras of cardinality \(2^{d+k}\).

**Exact endomorphism and retraction spectra.** The complete endomorphism image-overhead polynomial is \(\mathsf E_{\mathbf s}(u)=\mathsf H_{\mathbf s,\mathbf s}(u)\). The complete idempotent image-overhead polynomial is
\[
\boxed{\mathsf I_{\mathbf s}(u)=
\prod_{i=0}^{c-1}\sum_{j=0}^{s_i}\binom{s_i}{j}(j+1)^{s_i-j}u^j.}
\]
Every overhead \(0,1,\ldots,\sum_i s_i\) occurs as an idempotent image overhead, and there are exactly \(2^{\sum_i s_i}\) distinct embedded frame-retract supports.

**Reversal blindness, despite nonisomorphism.** For \(\rho(\mathbf s)_i=s_{-i\bmod c}\),
\[
\boxed{\mathsf E_{\mathbf s}(u)=\mathsf E_{\rho(\mathbf s)}(u),\qquad
\mathsf I_{\mathbf s}(u)=\mathsf I_{\rho(\mathbf s)}(u).}
\]
More generally, simultaneously reversing both source and target leaves preserves \(\mathsf H\) whenever the core lengths are fixed. Yet \(\mathbf C(\mathbf s)\) and \(\mathbf C(\rho(\mathbf s))\) need not be isomorphic as directed frames. For the two nonisomorphic \(9\)-world frames with cycle length \(3\) and leaf multiplicities \((1,2,3)\) and \((1,3,2)\), their common spectra are
\[
\mathsf E(u)=3+66u+397u^2+806u^3+564u^4+120u^5+12u^6,
\]
\[
\mathsf I(u)=1+17u+74u^2+107u^3+62u^4+14u^5+u^6.
\]
Thus each associated \(512\)-element Boolean modal algebra has \(1968\) endomorphisms and \(276\) idempotents. The two algebras are nonisomorphic, but even their *complete* endomorphism and idempotent image-rank polynomials agree. This is a failure of reconstruction from these natural numerical invariants, not a claim that the entire endomorphism monoids are isomorphic.

## Assumptions and scope

All frames are nonempty and finite, every point has *exactly one* successor, and each non-cycle world lies at distance one from a *single* directed core cycle. The orientation is fixed by the successor operation, not forgotten as an undirected graph. The vectors \(\mathbf s\) and \(\mathbf t\) are arbitrary finite vectors of nonnegative integers of their respective positive lengths; zero-leaf fibres are allowed. A bounded morphism \(f\) satisfies the exact successor-cone condition \(f[R(x)]=R(f(x))\). For a deterministic frame this is equivalent to commutation with its successor function. Different bijections of labelled leaf worlds count as different morphisms. Polynomial exponents count **frame-image leaf overhead**; the corresponding **algebra-image cardinalities** are powers of two and must not be confused with the frame cardinalities.

## Proof

**1. Cyclic obstruction and forced core map.** Write \(T\) and \(U\) for the source and target successor functions. A bounded morphism obeys \(fT=Uf\) because the successor sets are singletons. A source core point \(v_0\) has period \(c\), so \(f(v_0)\) has period dividing \(c\). The only periodic points in the target are its \(d\)-cycle, each with least period \(d\). Thus \(d\mid c\) is necessary. When it holds, every possible core map is the surjection \(f(v_i)=v'_{i+a\bmod d}\) for exactly one \(a\in\{0,\ldots,d-1\}\), and all \(d\) shifts work.

**2. Independent leaf choices.** A source leaf attached to \(v_i\) must map to a target world whose unique successor is \(v'_{i+a\bmod d}\). Its options are exactly the preceding core point \(v'_{i+a-1\bmod d}\) and the \(t_{i+a\bmod d}\) leaves attached to \(v'_{i+a\bmod d}\). No other constraints occur because there are no further predecessors to check. For fixed \(a\), the total number of source leaves assigned to a particular target fibre \(j\) is \(P_j^{(a)}\). These choices are independent across distinct fibres.

**3. Rank via inclusion–exclusion.** For \(p\) labelled inputs and \(q\) available target leaves, with one extra core option, choose exactly \(j\) target leaves to be occupied in \(\binom qj\) ways. Inclusion–exclusion over the \(j\) selected leaves gives \(\sum_{b=0}^{j}(-1)^{j-b}\binom jb(b+1)^p\) assignments using all \(j\) selected leaves (the core option is unrestricted). This establishes \(Q_{p,q}\), and multiplying it across all target fibres then summing over the \(d\) core shifts establishes \(\mathsf H\). Each such map already hits the entire target core, so the coefficient of \(u^k\) counts exactly \(d+k\) frame-image points.

**4. Idempotents and supports.** In an endomorphism, the shift \(a\) acts as a rotation on the core. Idempotence implies that rotation is the identity, hence \(a=0\). A target leaf present in the image of an idempotent map must be fixed by that map. Conversely, for any selected set of \(j\) leaves in source fibre \(i\), fix those leaves and let each of the \(s_i-j\) unselected leaves choose independently one of the \(j\) fixed leaves or the preceding core point. This gives \(\binom{s_i}{j}(j+1)^{s_i-j}\) idempotents with exactly \(j\) leaf-image points in fibre \(i\). Fibrewise multiplication proves \(\mathsf I\). Every selection of fixed leaves is feasible, hence all overheads occur and the distinct embedded retraction supports are precisely the core together with arbitrary subsets of the leaves.

**5. Orientation reversal and failure of reconstruction.** In the general Hom formula, reverse both vectors by replacing indices \(i\) with \(-i\), target indices \(j\) with \(-j\), and shift \(a\) with \(-a\). This is a termwise bijection between the summands and factors of the two polynomials. For self-Hom this proves the \(\mathsf E\) identity; \(\mathsf I\) is invariant under any permutation of fibres. Any directed-frame isomorphism must preserve the periodic core, on which it commutes with the cyclic successor; it is therefore a rotation. Hence \(\mathbf C(\mathbf s)\cong\mathbf C(\mathbf t)\) holds exactly when \(\mathbf t\) is a cyclic rotation of \(\mathbf s\). The vectors \((1,2,3)\) and \((1,3,2)\) are reversals but not rotations; the displayed coefficient arrays follow by direct substitution.

**6. Algebraic transfer.** The inverse-image map induced by a bounded morphism preserves Boolean operations and \(\Box\); conversely every homomorphism between the finite full-powerset Boolean modal algebras arises from exactly one function preserving the successor operation. For any function \(f:X\to Y\), its inverse-image Boolean algebra consists precisely of unions of the nonempty fibres of \(f\), hence has \(2^{|f[X]|}\) elements. A modal-algebra isomorphism induces a directed-frame isomorphism, so the two example algebras are also nonisomorphic.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The standalone operation-table checker enumerates **all** functions on \(56\) small deterministic frames, testing \(1{,}262{,}096\) function tables directly against the commuting-successor condition. It compares the exact endomorphism and idempotent rank distributions with the formulas, separately enumerates \(225\) source-target frame pairs (\(22{,}183\) candidate function tables), and checks \(15\) small cases by direct Boolean modal-algebra preservation. A separate normal-form enumeration checks \(1968\) maps for each of the two nonisomorphic nine-world examples. Reflection invariance is checked on every finite test configuration. All computations use integer arithmetic. The verifier's exact successful summary is in `VERIFICATION.md`. The exhaustive finite tests support, but do not replace, the general proof above.

## Relationship to prior work

The coalgebraic modal-algebra/frame dualities in Bezhanishvili, Bezhanishvili and de Groot (2021/2022) supply the categorical setting and are **not** new here. Their work establishes broader dualities but does not enumerate bounded homomorphism image ranks for the present cycle-and-leaf frames. Jakubíková-Studenovská and Potpinková (2014) explicitly study possible endomorphism image cardinalities of finite monounary algebras; those *support sets*, along with general one-unary algebra homomorphism theory, are also prior art. The contribution claimed here is the joint source-target **multiplicity** polynomial, its dual modal-algebra interpretation, the idempotent rank refinement, and the counterexample to rank-profile reconstruction under orientation reversal.

Dimitrova, Fernandes, Koppitz and Quinteiro (2023) study endomorphism monoids of **undirected** cycle graphs. Their graph homomorphisms are not the successor-commuting maps of a deterministic directed Kripke frame and their main invariants are monoid generators, Green relations, regularity, and cardinalities rather than the present decorated-cycle Hom-rank polynomial. General older monounary-algebra literature may implicitly contain a specialization of the normal form; novelty is not inferred merely from unsuccessful searches. The concrete joint polynomial and reversal-reconstruction distinction are the specifically delimited claims.

## Limitations

This result concerns a single cyclic core and depth-one leaves; it does not classify arbitrary functional digraphs, higher-depth trees, multiple-cycle frames, or nonfunctional Kripke relations. It does not show that the two nonisomorphic examples have isomorphic endomorphism monoids, only identical image-rank distributions. A complete examination of the 1985–1986 general monounary-endomorphism articles was not available, so an implicit antecedent remains possible.

## References

1. G. Bezhanishvili, N. Bezhanishvili and J. de Groot, *A Coalgebraic Approach to Dualities for Neighborhood Frames*, first submitted 2021-06-03, arXiv:2106.01628; *Logical Methods in Computer Science* 18(3), 4 (2022), doi:10.46298/lmcs-18(3:4)2022. Sections 1–2 give the finite-frame/modal-algebra duality setting.
2. D. Jakubíková-Studenovská and K. Potpinková, *The endomorphism spectrum of a monounary algebra*, *Mathematica Slovaca* 64 (2014), 675–690, doi:10.2478/s12175-014-0233-7; associated 2014 presentation at https://im.saske.sk/ssaos2014/talks/monday/Studenovska.pdf.
3. D. Jakubíková-Studenovská, *Endomorphisms and connected components of partial monounary algebras*, *Czechoslovak Mathematical Journal* 35 (1985), 467–490, doi:10.21136/CMJ.1985.102036.
4. D. Jakubíková-Studenovská, *Endomorphisms of partial monounary algebras*, *Czechoslovak Mathematical Journal* 36 (1986), 376–392, doi:10.21136/CMJ.1986.102100.
5. I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, first submitted 2023-10-06, arXiv:2310.04149.
