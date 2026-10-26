# Two-jump rigidity and a sharp three-speed threshold for minimal Cantor dynamics

## Finding
Let \(X\) be a Cantor space and \(T:X\to X\) a minimal homeomorphism. For integers \(1\le a<b\), set \(d=b-a\). If \(p:X\to\{a,b\}\) is continuous and \(S(x)=T^{p(x)}x\), then the following are equivalent:

1. \(S\) is a homeomorphism of \(X\).
2. \(p\circ T^d=p\).

Whenever these hold, define
\[
 k(x)=\sum_{j=0}^{d-1}\mathbf 1_{\{p=b\}}(T^j x).
\]
The integer \(k(x)\) is independent of \(x\), and each \(T\)-orbit splits into **exactly** \(a+k\) distinct \(S\)-orbits. Thus nonconstant two-valued homeomorphic speedups with these particular two jump values exist if and only if \(T^d\) is not minimal, equivalently if there is a finite cyclic factor of order greater than one dividing \(d\).

If \(T\) is totally minimal (every positive power is minimal), then every homeomorphic speedup with at most two positive jump values has a constant jump. Conversely, **every** totally minimal Cantor homeomorphism admits a **minimal**, homeomorphic speedup with exactly three jump values \(\{1,2,3\}\), conjugate to \(T^2\). Three is the sharp minimum size of a nonconstant jump alphabet, and three is the smallest possible maximum jump for a nonconstant speedup.

## Assumptions and scope
The space is nonempty, compact, metrizable, perfect and zero-dimensional. The homeomorphism \(T\) is minimal, hence all its orbits are infinite and every invariant Borel probability measure has full support. A continuous integer-valued jump function is locally constant and its image is finite. A speedup here means **an invertible continuous map** of the form \(S(x)=T^{p(x)}x\) with positive integer-valued \(p\). The two-value theorem does **not** assume the speedup itself is minimal. The final three-value existence statement assumes total minimality and does ensure minimality of the speedup. Orbit number refers to distinct bi-infinite \(S\)-orbits contained in one \(T\)-orbit.

## Proof
**Necessity.** Write \(B=p^{-1}(\{b\})\), a clopen set. If \(x\in B\) and \(T^d x\notin B\), then \(p(x)=b\) and \(p(T^d x)=a\), so
\[
 S(x)=T^b x=T^{a+d}x=S(T^d x).
\]
Minimality on a Cantor space implies the points \(x\) and \(T^d x\) are distinct. Thus injectivity forces \(T^dB\subseteq B\). Let \(\mu\) be a \(T\)-invariant Borel probability measure, which exists by compactness. Its support is a nonempty closed \(T\)-invariant set, hence all \(X\) by minimality. Invariance gives \(\mu(T^dB)=\mu(B)\). The difference \(B\setminus T^dB\) is clopen and has measure zero, so it is empty. Therefore \(T^dB=B\) and \(p\circ T^d=p\).

**Sufficiency.** On any infinite orbit \(\{T^n x:n\in\mathbb Z\}\), define \(p_n=p(T^nx)\). The condition means \(p_{n+d}=p_n\). The restriction of \(S\) is equivalent to \(f(n)=n+p_n\). For each residue class \(r\pmod d\), the entire class is sent by \(f\) bijectively onto the class \(r+a\pmod d\), because the jump is constant on the source class and both possibilities differ by \(d\). Since \(r\mapsto r+a\) permutes residues, \(f\) is a permutation of \(\mathbb Z\). Hence \(S\) is bijective on every orbit and therefore on \(X\). It is continuous by construction; compactness of \(X\) and Hausdorffness make the inverse continuous.

**Exact orbit number.** For a fixed orbit, the positive map \(f(n)>n\) is a permutation. Its bi-infinite orbits increase strictly and are unbounded in both directions. Thus each meets the boundary between negative and nonnegative integers exactly once, and the number of such orbits is the number of crossings \(n<0\le n+p_n\). There are exactly \(a\) crossings from \(-a\le n<0\), and there are additionally precisely \(k\) crossings from the remaining interval \(-b\le n<-a\) of length \(d\), namely at its positions with \(p_n=b\). So the number is \(a+k\). The integer function \(k(x)\) is continuous and \(T\)-invariant, since its summands rotate cyclically under \(T\) using \(p\circ T^d=p\). Minimality forces it constant.

**Cyclic-factor equivalence.** If \(T^d\) has a proper nonempty clopen invariant set \(B\), assigning jump \(b\) on \(B\) and \(a\) off it constructs a nonconstant homeomorphic speedup by the equivalence just proved. Conversely a nonconstant homeomorphic two-valued speedup provides such a set. More generally, if \(T^d\) is not minimal, choose a proper minimal set \(Y\) for \(T^d\). The at most \(d\) distinct sets \(Y,TY,\ldots,T^{d-1}Y\) are pairwise disjoint or equal, because all are minimal for \(T^d\). Their union is a nonempty closed \(T\)-invariant set, hence equals \(X\). They are therefore clopen components cyclically permuted by \(T\), and the number \(g\) of components is a divisor of \(d\) greater than one. This gives the asserted cyclic factor. Conversely a nontrivial cyclic factor of order dividing \(d\) gives a proper clopen \(T^d\)-invariant fiber.

**Sharp positive three-value construction.** Suppose \(T\) is totally minimal. Since every \(T^d\) is minimal, the two-value equivalence forces any homeomorphic speedup using at most two jump values to be constant. Choose a nonempty clopen set \(A\) for which \(T^j A\), \(-4\le j\le4\), are pairwise disjoint. Such a set exists because \(T\) is aperiodic and \(X\) is zero-dimensional. Define the clopen transposition \(R\) by \(R|_A=T|_A\), \(R|_{TA}=T^{-1}|_{TA}\), and \(R\) is the identity elsewhere. Then \(R^2=\mathrm{id}\). Put \(S=R\circ T^2\circ R\), and let \(q(x)=1\) on \(A\), \(q(x)=-1\) on \(TA\), and \(q(x)=0\) elsewhere. The orbit cocycle of the conjugate is
\[
 p(x)=2+q(x)+q(T^{2+q(x)}x).
\]
For \(x\in A\), its second \(q\)-term is zero because \(T^3A\) avoids \(A\cup TA\); hence \(p=3\). For \(x\in TA\), the second term is zero because \(T^2A\) avoids \(A\cup TA\); hence \(p=1\). For all remaining points \(q(x)=0\), so \(p(x)\in\{1,2,3\}\). In particular \(p=2\) on the nonempty set \(T^2A\), since \(T^2A,T^4A\) avoid \(A\cup TA\). Thus all three values occur. Every jump is positive, \(S\) is a homeomorphism, and it is conjugate to \(T^2\) via the involution \(R\). Total minimality makes \(T^2\), and therefore \(S\), minimal. No nonconstant positive jump function can have maximum below three, by the lower bound; this construction attains three.

## Verification
The included standalone Python script `verify.py` exhaustively checks all \(48{,}960\) binary assignments on finite cyclic systems of orders \(3\) through \(10\), first jumps \(1\) through \(4\), and gaps \(1\) through \(6\), comparing bijectivity to invariance under the gap power. It also checks the transposition construction and the full jump alphabet on six finite cyclic proxies with orders \(11,13,17,19,23,29\). These checks returned `VERIFY_OK`. The infinite theorem follows from the preceding proof; finite cyclic tests do not prove its infinite quantifiers, its minimality, or novelty.

## Relationship to prior work
Bruin's recent work (arXiv:2602.13652, initially posted 2026-02-14) studies linearly recurrent subshifts under **already homeomorphic** speedups and establishes linear recurrence of transitive speedups. Its hypotheses and principal theorems do not give the two-valued homeomorphism criterion or a universal minimum number of jump values. The older work of Alvin–Ash–Ormes (arXiv:1610.03537, Section 2) introduces bounded speedups and proves that the number of subordinate speedup orbits is constant, but does not provide the explicit two-valued rigidity criterion here. Importantly its Section 4.3.1 **already constructs one example** using the values \(\{1,2,3\}\); existence of a three-valued example per se is **not** claimed new. What is asserted here is the universal sharp threshold for every totally minimal Cantor system together with the if-and-only-if characterization for each prescribed pair of jumps and the exact arithmetic orbit count. Ash–Ormes (arXiv:2208.07854) provides broad characterizations via dimension groups and strong speedups; the present elementary classification concerns a different, fixed small jump-range question. These comparisons are based on inspected primary texts, but do not prove global historical uniqueness.

## Limitations
The two-value theorem assumes minimality of \(T\) and continuity of \(p\). It does not claim that a two-valued homeomorphic speedup is minimal. The universal three-value statement requires **total** minimality, although other constructions may exist without it. The exact orbit-number formula is for aperiodic Cantor orbits, not an arbitrary finite periodic action. The finite verifier is supplementary. Priority may be affected by older results phrased in topological-full-group or orbit-cocycle terminology; no independent audit has been performed.

## References
1. H. Bruin, *Speedups of linearly recurrent subshifts*, arXiv:2602.13652, initial public posting 2026-02-14, https://arxiv.org/abs/2602.13652.
2. L. Alvin, D. D. Ash, N. S. Ormes, *Bounded Topological Speedups*, arXiv:1610.03537 (2016); Section 2 and Section 4.3.1, https://arxiv.org/abs/1610.03537.
3. D. D. Ash, N. S. Ormes, *Topological Speedups For Minimal Cantor Systems*, arXiv:2208.07854 (2022); introduction and main theorem, https://arxiv.org/abs/2208.07854.
