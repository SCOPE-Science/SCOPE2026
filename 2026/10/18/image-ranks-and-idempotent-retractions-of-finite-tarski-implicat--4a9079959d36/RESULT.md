# Image ranks and idempotent retractions of finite Tarski implication algebras

## Finding
For every integer \(n\ge2\), put \(X=[n]\) and let \(\mathcal I_n=\mathcal P(X)\setminus\{\varnothing\}\), with the *implication-only* operation
\[
A\Rightarrow B=(X\setminus A)\cup B.
\]
An endomorphism is a map \(F:\mathcal I_n\to\mathcal I_n\) preserving \(\Rightarrow\); its **image rank** is the number \(|F(\mathcal I_n)|\) of distinct output sets. Then every endomorphism is uniquely represented by a pointed function \(\theta:X\cup\{0\}\to X\cup\{0\}\), \(\theta(0)=0\), as
\[
F_\theta(A)=\{j\in X: \theta(j)=0\text{ or }\theta(j)\in A\}.
\]
Exactly two kinds of restrictions \(\theta|_X\) are allowed: a permutation of \(X\), or a function that takes the value \(0\) at least once. The composition law is \(F_\theta\circ F_\eta=F_{\eta\circ\theta}\).

The automorphisms are precisely the \(n!\) permutations, each of image rank \(2^n-1\). Every other endomorphism has image **a Boolean lattice**, with image rank \(2^r\) for exactly one \(0\le r\le n-1\). If \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) denotes a Stirling number of the second kind, the exact rank counts are
\[
\boxed{N_{n,r}=\binom nr(r+1)!\left\{\begin{matrix}n\\r+1\end{matrix}\right\},\quad 0\le r<n},\qquad
\boxed{N_{n,\mathrm{unit}}=n!}.
\]
In particular,
\[
|\operatorname{End}(\mathcal I_n)|=(n+1)^n-n^n+n!.
\]
The exact counts of **idempotent** endomorphisms \(F\circ F=F\), classified by image rank, are
\[
\boxed{E_{n,r}=\binom nr\big((r+1)^{n-r}-r^{n-r}\big),\quad 0\le r<n},\qquad
\boxed{E_{n,\mathrm{unit}}=1}.
\]
Thus each of the sizes \(1,2,4,\ldots,2^{n-1},2^n-1\) is actually attained both by an endomorphism and by an idempotent endomorphism. These are exact formulas for *all* finite carrier sizes, not merely low-dimensional data.

## Assumptions and scope
The carrier contains all nonempty subsets of \(X\), not the empty set. Its operation \(\Rightarrow\) is classical material implication relative to \(X\); an endomorphism need not preserve a nonexistent bottom element. We count actual functions on this fixed labelled algebra, not maps modulo conjugacy. The empty-set symbol \(0\) used in \(\theta\) is a **new sentinel**, not an element of \(\mathcal I_n\). A Boolean image is a Boolean algebra under its inherited lattice operations, with its own least element; it need not contain \(\varnothing\).

## Proof
**1. Join and existing meets are preserved.** In this Tarski algebra, \(A\cup B=(A\Rightarrow B)\Rightarrow B\). Hence every endomorphism preserves unions, the order, and \(X=A\Rightarrow A\). Whenever \(C=A\cap B\ne\varnothing\), the principal interval \([C,X]\) is a Boolean lattice whose complement of \(Y\supseteq C\) is \(Y\Rightarrow C\). Therefore
\[
A\cap B=\big((A\Rightarrow C)\cup(B\Rightarrow C)\big)\Rightarrow C.
\]
Apply \(F\). Since \(F(C)\subseteq F(A),F(B)\), the same relative-complement identity in \([F(C),X]\) yields \(F(A\cap B)=F(A)\cap F(B)\). This step does not assume preservation of a nonexistent empty meet.

**2. Coordinate filters.** For each output coordinate \(j\in X\), let
\[
I_j=\{i\in X:j\in F(\{i\})\}.
\]
Because \(F\) preserves nonempty unions and sends \(X\) to \(X\), each \(I_j\) is nonempty and \(j\in F(A)\) precisely when \(A\cap I_j\ne\varnothing\). Suppose \(I_j\) has at least two elements \(s\ne t\) and omits some \(u\in X\). For \(A=\{s,u\}\) and \(B=\{t,u\}\), both outputs contain \(j\), but \(A\cap B=\{u\}\) and \(F(\{u\})\) does not contain \(j\). This contradicts existing-meet preservation. Therefore each \(I_j\) is either a singleton or all of \(X\). Set \(\theta(j)=i\) in the singleton case and \(\theta(j)=0\) in the all-of-\(X\) case. This proves the formula for \(F_\theta\) and uniqueness of \(\theta\).

If no output coordinate has \(\theta(j)=0\), then the nonemptiness of every \(F(\{i\})\) requires each \(i\) to occur among the \(n\) values of \(\theta|_X\), making it a permutation. Conversely, if \(0\) occurs, the formula is everywhere nonempty. For \(\theta(j)=0\), coordinate \(j\) is always true, and for \(\theta(j)=i\ne0\), coordinate truth is the input truth at \(i\). In either case material implication is preserved coordinatewise. This proves the classification and converse. Direct substitution proves the stated reversed composition law.

**3. Image is a cube or the punctured cube.** In the permutation case \(F_\theta\) permutes coordinates, so its image is the whole \(2^n-1\)-element algebra. Otherwise let \(U=\theta^{-1}(0)\ne\varnothing\), let \(R=\theta(X)\setminus\{0\}\), and write \(r=|R|\le n-1\). For \(i\in R\), put \(B_i=\theta^{-1}(i)\). The nonempty sets \(U,B_i\) are disjoint, and for \(A\in\mathcal I_n\),
\[
F_\theta(A)=U\cup\bigcup_{i\in A\cap R}B_i.
\]
Every subcollection of the \(r\) blocks occurs. In particular the empty subcollection occurs using the singleton \(A=\{u\}\) with \(u\notin R\), which exists since \(r<n\). Consequently the image is a Boolean \(r\)-cube above bottom \(U\), of size \(2^r\).

**4. Exact rank enumeration.** For \(r<n\), choose the occupied nonzero labels \(R\subseteq X\) in \(\binom nr\) ways. The function \(\theta|_X:X\to R\cup\{0\}\) must be onto all \(r+1\) named values, including \(0\). The number of surjections is \((r+1)!\left\{\begin{smallmatrix}n\\r+1\end{smallmatrix}\right\}\). The \(n!\) remaining maps are permutations. Summing also counts all functions from \(X\) to \(X\cup\{0\}\) that use \(0\), namely \((n+1)^n-n^n\).

**5. Idempotent enumeration.** Uniqueness and the composition law imply \(F_\theta^2=F_\theta\iff\theta^2=\theta\). A nonpermutation idempotent with \(|R|=r\) fixes every value in \(R\) as well as \(0\). Choose \(R\) in \(\binom nr\) ways; each of the other \(n-r\) points maps to \(R\cup\{0\}\), and at least one maps to \(0\). This gives \((r+1)^{n-r}-r^{n-r}\) possibilities. An idempotent permutation is the identity. The formulas include \(r=0\) with the standard convention \(0^m=0\) for positive \(m\).

## Verification
The accompanying self-contained Python file `verify.py` has no third-party dependencies. Run `python3 verify.py`. It independently enumerates all join-generated maps of \(\mathcal I_n\) for \(n=2,3,4\), tests the *defining implication identity* for every nonempty input pair, computes image sizes and idempotency directly, and separately enumerates the pointed-function forms. All agree with the Stirling and idempotent formulas. It prints `VERIFY_OK`. Exact finite checks are supporting diagnostics; the preceding proof establishes the formulas for every \(n\ge2\).

## Relationship to prior work
Gaitán's work on endomorphisms of implication/Tarski algebras (2012, 2014, 2015) proves general reconstruction results, including the importance of maximal filters and the endomorphism monoid. The general correspondence between Tarski algebras and semi-Boolean algebras is classical. González and Calomino (2021) represent finite distributive nearlattices and explicitly define nearlattice homomorphisms preserving existing meets. The pointed-coordinate representation in this special family follows the established partial-transformation viewpoint and is not claimed as an independently new duality. The contribution assessed here is the *complete exact image-rank distribution, Boolean-image dichotomy, and rank-resolved idempotent census* for the implication reduct of a punctured Boolean cube.

## Limitations
The theorem concerns this concrete family, not arbitrary finite Tarski algebras or arbitrary nearlattices. It counts labelled endomorphisms, not their isomorphism or conjugacy classes. Earlier semigroup or duality literature could imply the exact rank/idempotent formulas by a different route; a 2012 primary article was not accessible in full. The published-priority assessment is therefore conditional on the primary literature inspected and does not claim exhaustive historical novelty. The computational verification ranges only through \(n=4\).

## References
- H. Gaitán, *Finite Tarski algebras are determined by their endomorphisms*, Semigroup Forum 84 (2012). DOI: 10.1007/s00233-011-9345-3. Abstract consulted; complete text not available.
- H. Gaitán, *Endomorphisms of implication algebras*, Demonstratio Mathematica 47 (2014). DOI: 10.2478/dema-2014-0022. Accessible primary full text inspected.
- H. Gaitán, *Endomorphisms and subalgebras of Tarski algebras*, Reports on Mathematical Logic 50 (2015), 31–39. DOI: 10.4467/20842589RM.15.002.3911. https://rml.tcs.uj.edu.pl/rml-50/2-gaitan.pdf
- L. J. González and I. Calomino, *Finite distributive nearlattices*, arXiv:2106.00807, first public version 2021-06-01. https://arxiv.org/abs/2106.00807
