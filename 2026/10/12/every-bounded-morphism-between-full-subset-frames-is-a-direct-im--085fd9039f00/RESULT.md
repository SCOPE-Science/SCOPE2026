# Every bounded morphism between full subset frames is a direct-image map

## Finding

For every pair of nonempty sets \(X,Y\), define the (possibly infinite) full subset Kripke frame
\[
\mathsf P_X=(\mathcal P(X)\setminus\{\varnothing\},\supseteq).
\]
A frame \(p\)-morphism \(F:\mathsf P_X\to\mathsf P_Y\) means an order-preserving map satisfying the exact upward-lifting condition: whenever \(F(A)\supseteq T\ne\varnothing\), with \(T\subseteq Y\), there exists nonempty \(B\subseteq A\) such that \(F(B)=T\).

**Classification theorem.** Every such \(F\) has the unique form
\[
F(A)=c[A]=\{c(x):x\in A\}
\]
for a function \(c:X\to Y\), and conversely every function \(c:X\to Y\) defines a \(p\)-morphism this way. Direct-image formation preserves identity maps and composition. Thus the category of nonempty sets and functions is isomorphic to the category of these explicitly represented subset frames and \(p\)-morphisms (and equivalent to the abstract full-subset-frame category).

For finite \(|X|=n\ge1\) and \(|Y|=m\ge1\), this yields exactly \(m^n\) \(p\)-morphisms. Exactly the surjective functions produce onto \(p\)-morphisms, giving the precise onto-morphism count
\[
 m!\,{n\brace m}
 =\sum_{j=0}^{m}(-1)^j\binom mj(m-j)^n,
\]
where \({n\brace m}\) is a Stirling number of the second kind (zero when \(n<m\)). Every non-onto morphism has as its image the generated subframe on \(c[X]\), so it factors through a surjective morphism onto that generated subframe.

## Assumptions and scope

Here \(\mathcal P(X)\) contains **all** subsets, including infinite subsets when \(X\) is infinite; the empty subset is removed. A world \(A\) accesses exactly the nonempty subsets of \(A\) under the reflexive and transitive Kripke order \(\supseteq\). Frame morphisms need **not** be onto unless explicitly called onto. No valuations, probability measures, generated-subframe restriction on the domain, or choice principles are required. The theorem applies to finite and infinite nonempty underlying sets. It does **not** assert the same characterization for arbitrary rooted posets, truncated powersets, or the generalized topless products of arbitrary finite frames.

## Proof

**Step 1: maximal worlds determine a map of underlying sets.** Each singleton \(\{x\}\) is a maximal world of \(\mathsf P_X\), and these are exactly the maximal worlds. Any \(p\)-morphism takes maximal worlds to maximal worlds: if a world \(U\) is maximal, and \(F(U)\) had a strict successor \(T\), the back condition would require a successor of \(U\) mapping to \(T\), whereas the only successor of \(U\) is itself. Therefore each \(F(\{x\})\) is a singleton \(\{c(x)\}\). This uniquely defines a function \(c:X\to Y\).

**Step 2: no further choices at nonsingleton worlds.** Let nonempty \(A\subseteq X\). For each \(x\in A\), monotonicity from \(A\supseteq\{x\}\) gives \(F(A)\supseteq F(\{x\})=\{c(x)\}\); hence \(c[A]\subseteq F(A)\). Conversely, take \(y\in F(A)\). Since \(F(A)\supseteq\{y\}\), upward lifting produces a nonempty \(B\subseteq A\) with \(F(B)=\{y\}\). Choose any \(x\in B\). Monotonicity from \(B\supseteq\{x\}\) gives \(\{y\}=F(B)\supseteq\{c(x)\}\); thus \(y=c(x)\in c[A]\). Therefore \(F(A)=c[A]\) for every \(A\).

**Step 3: every direct-image map satisfies both morphism laws.** For any function \(c:X\to Y\), direct images preserve inclusions, so \(F_c(A)=c[A]\) is order preserving. If \(\varnothing\ne T\subseteq c[A]\), define \(B=A\cap c^{-1}[T]\). This \(B\) is nonempty, satisfies \(B\subseteq A\), and has exactly \(c[B]=T\). This is the back condition. The construction is explicit, including for infinite sets, and does not require simultaneously choosing representatives of fibers.

**Step 4: categorical and counting conclusions.** The equality \(F_d(F_c(A))=d[c[A]]=(d\circ c)[A]=F_{d\circ c}(A)\) and \(F_{\mathrm{id}_X}=\mathrm{id}_{\mathsf P_X}\) proves compatibility with composition and identities. Steps 1--3 give a bijection on every hom-set, establishing the stated category description. The image is \(\{T:\varnothing\ne T\subseteq c[X]\}\), exactly the generated subframe rooted at \(c[X]\). Thus \(F_c\) is onto \(\mathsf P_Y\) if and only if \(c[X]=Y\). For finite sizes \(n,m\), there are \(m^n\) functions and \(m!\,{n\brace m}\) surjections, the latter also following from inclusion-exclusion over omitted points of \(Y\).

## Verification

The accompanying self-contained Python 3 checker `verify_medvedev.py` enumerates every set map between the **world sets** (not just candidate maps induced by functions) for \(1\le n,m\le3\), checks the forth/back condition directly at each world, and compares the resulting maps with those obtained from every function between underlying sets. It also independently checks onto-morphism counts. It tested **826,113** maps between world sets, found exactly **56** \(p\)-morphisms across these nine pairs of sizes, and printed `VERIFY_OK`. Run `python3 verify_medvedev.py` from the extracted package directory. This finite check is corroboration only; the universal and infinite assertions follow from the preceding proof.

## Relationship to prior work

Han Xiao's 2026 paper defines Medvedev frames as topless products of two-element chains, recalls \(p\)-morphisms, and applies them to generalized Medvedev-logics problems; its inspected main results do not classify all morphisms between the original full subset frames. Nicola Vio's 2023 thesis, Section 6.3, explicitly constructs automorphisms from permutations of singleton maximal worlds (Lemma 6.22), a retraction between successive frame sizes (Lemma 6.24), and a modular-reduction \(p\)-morphism from \(\mathsf P_{kn}\) onto \(\mathsf P_n\) (Lemma 6.25). Those are previously known members of the maps classified here and are **not** claimed as new. Ivano Ciardelli's 2009 thesis identifies singleton maximal worlds and the saturation property of finite Medvedev frames. Zalán Gyenis's 2018 article also defines infinite full-subset Medvedev frames and studies bounded morphisms into them from probability frames. The contribution here is the exact **all-morphism** correspondence for every pair of full subset frames (including infinite ones), together with its complete finite hom-set and onto-hom-set enumerations.

## Limitations

The characterization depends crucially on every nonempty subset being present; it is not a classification of \(p\)-morphisms between arbitrary generalized Medvedev frames. The finite counts enumerate labeled underlying sets; unlabeled quotient counts require a separate equivalence relation. The proof does not establish novelty against every historical reference; a formulation using semilattices, bounded morphisms, or dual categories may already exist. Independent mathematical review has not been performed. Exhaustive computation through size three does not certify claims for larger or infinite sets.

## References

- Han Xiao, *Non-finite Axiomatizability of Generalized Medvedev Logics*, arXiv:2606.31893 (initially submitted 2026-06-30), EPTCS 447 (2026), 770--781, https://arxiv.org/abs/2606.31893 .
- Nicola Vio, *Unification and Structural Completeness in Intermediate Logics*, doctoral thesis (2023), Section 6.3, especially Lemmas 6.22--6.25, https://tesidottorato.depositolegale.it/bitstream/20.500.14242/123594/1/Vio_thesis.pdf .
- Ivano Ciardelli, *Inquisitive Semantics and Intermediate Logics*, 2009 thesis, Section 3.4.1, https://eprints.illc.uva.nl/id/document/1920 .
- Zalán Gyenis, *On the Modal Logic of Jeffrey Conditionalization*, Logica Universalis (2018), Section 4, https://real.mtak.hu/87067/1/Gyenis-2018-Logica_Universalis.pdf .
