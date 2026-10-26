# An effective first-order convergence law and dense limiting-probability spectrum for two independent involutions

## Finding
Let \(f_n,g_n\) be independent, uniformly sampled involutions of the finite set \([n]\). Regard the pair as a structure in the language of two unary function symbols (equivalently, their binary graphs). Then, for every fixed first-order sentence \(\varphi\), the limit \(\lim_{n\to\infty}\Pr(([n],f_n,g_n)\models\varphi)\) exists and is effectively computable. There is an effectively determined positive integer \(D\) for which this limit belongs to \(\mathbb Q[e^{-1/D}]\). The set of all these limiting probabilities, as \(\varphi\) varies, is dense in \([0,1]\); in particular this is a convergence law, not a zero–one law.

More precisely, the possible probabilities are **exactly** the probabilities of events described by finite Boolean combinations of assertions \(Z_t\ge h\), for integer \(h\ge1\), where the random variables \((Z_t)\), indexed by the alternating component types described below, are mutually independent Poisson variables of means \(w_t\) equal to \(1\), \(1/2\), or \(1/(2k)\), as appropriate. This statement is a characterization of the limit-probability spectrum, not a claim that any individual sentence is itself a fixed local event.

For example, if \(F\subseteq\mathbb N_{\ge1}\) is finite, the property that a component is an alternating cycle of length \(2k\) for some \(k\in F\) has limiting probability
\[
1-\exp\Bigl(-\sum_{k\in F}\frac1{2k}\Bigr).
\]
These probabilities form a dense subset of \([0,1]\).

## Assumptions and scope
An **involution** is a permutation \(f\) satisfying \(f^2=\operatorname{id}\), possibly with fixed points. Both involutions are sampled independently and uniformly from the set of **all** involutions on \([n]\); neither is conditioned to be fixed-point-free or to commute with the other. Each nonfixed application of \(f\) or \(g\) is drawn as an edge of its own color; a fixed point is understood as a self-loop of that color.

Every connected component in the resulting two-colored multigraph is one of the following types. For each odd \(s\ge1\), there is one alternating path type \(P_s\), with \(s\) vertices and component weight \(w(P_s)=1\). For each even \(s\ge2\), there are two path types \(P_s^f,P_s^g\), distinguished by which involution fixes both endpoints, each of component weight \(w(P_s^f)=w(P_s^g)=1/2\). Finally, for every integer \(k\ge1\), there is one alternating cycle type \(Q_k\) on \(2k\) vertices, with \(w(Q_k)=1/(2k)\). The case \(k=1\) is the valid two-vertex component with a pair of differently colored edges between its two vertices. The vertex size of a type \(t\) is denoted by \(s_t\).

Let \(C_{t,n}\) be the number of components of type \(t\). For every finite set \(T\) of types, the vector \((C_{t,n})_{t\in T}\) converges jointly to independent Poisson variables \((Z_t)_{t\in T}\) with respective means \((w_t)_{t\in T}\).

## Proof
**1. Exact component enumeration and factorial moments.** The labeled count for a fixed path with \(s\) vertices is \(s!\) when \(s\) is odd (including the one-vertex case), and \(s!/2\) for each of the two types when \(s\) is even; the labeled count for an alternating \(2k\)-cycle is \((2k)!/(2k)\). Thus the exponential generating function for ordered pairs of involutions is
\[
A(z)=\exp\Bigl(\sum_{t}w_tz^{s_t}\Bigr)=
\exp\Bigl(\frac{z}{1-z}\Bigr)(1-z^2)^{-1/2}.
\]
Write \(I_n\) for the number of involutions on \([n]\), and \(a_n=[z^n]A(z)=I_n^2/n!\). For every fixed finite vector \((m_t)_{t\in T}\) of nonnegative integers, with \(S=\sum_{t\in T}s_tm_t\), marking distinct components by type and differentiating the finite-variable exponential generating function gives the **exact** identity
\[
\mathbb E\prod_{t\in T}(C_{t,n})_{m_t}=
\Bigl(\prod_{t\in T}w_t^{m_t}\Bigr)\frac{a_{n-S}}{a_n}
\quad(n\ge S),
\]
where \((x)_m=x(x-1)\cdots(x-m+1)\). For \(n<S\), the left side is zero. This identity also applies when \(T\) includes both even-path endpoint-color types or the doubled-edge cycle type.

**2. Elementary coefficient-ratio limit.** The involution numbers satisfy \(I_0=I_1=1\) and \(I_n=I_{n-1}+(n-1)I_{n-2}\). If \(u_n=I_n/I_{n-1}\), then \(u_1=1\) and \(u_n=1+(n-1)/u_{n-1}\). Induction gives \(\sqrt n\le u_n\le1+\sqrt n\): the upper bound uses \(u_{n-1}\ge\sqrt{n-1}\), and the lower bound uses \(u_{n-1}\le1+\sqrt{n-1}\) and \(1+t^2/(t+1)\ge\sqrt{t^2+1}\) for \(t=\sqrt{n-1}\). Consequently, \(u_n^2/n\to1\), and for every fixed \(S\),
\[
\frac{a_{n-S}}{a_n}=\frac{n(n-1)\cdots(n-S+1)}{u_n^2u_{n-1}^2\cdots u_{n-S+1}^2}\longrightarrow1.
\]
The joint factorial moments therefore converge to \(\prod_{t\in T}w_t^{m_t}\), the moments of independent Poisson variables. Since the limiting multivariate Poisson moment generating function is entire, the multivariate method of moments proves the joint distributional convergence.

**3. Logical locality and exhaustiveness.** Fix a first-order sentence \(\varphi\). The structures have Gaifman degree at most \(2\); self-loops contribute no new distinct neighbors. The effective bounded-degree Hanf theorem yields a radius \(r\) and threshold \(h\) such that the truth of \(\varphi\) depends only on the counts of rooted radius-\(r\) neighborhood types, each truncated at \(h\). For any fixed \(r\), a radius-\(r\) type that occurs only in bounded-size path/cycle components is a deterministic, explicitly calculable linear combination of finitely many \(C_{t,n}\). Every other realizable neighborhood type is either an interior type on arbitrarily long paths or an endpoint-adjacent type on arbitrarily long paths. Each such type occurs, with probability tending to one, at least \(h\) times: for any prescribed \(L\), pick \(L\) distinct sufficiently long path sizes of a suitable parity and endpoint-color type. Their component counts converge jointly to independent Poisson variables of means \(1\) or \(1/2\); by taking \(L\) sufficiently large, the probability of having fewer than \(h\) such occurrences becomes arbitrarily small. Thus all these neighborhood counts are saturated at \(h\) with probability tending to one.

It follows that the asymptotic truth value of \(\varphi\), up to an event of probability tending to zero, is a finite Boolean function of the truncated counts of the **finitely many small connected component types**. Step 2 proves convergence of its probability, and the independent Poisson law makes that limit effectively computable. Each \(w_t\) is rational, so the probabilities of the finitely many Poisson thresholds and their Boolean combinations are rational combinations of \(e^{-w_t}\); choosing a common denominator \(D\) puts the result in \(\mathbb Q[e^{-1/D}]\).

Conversely, for every fixed component type \(t\) and \(h\ge1\), a first-order sentence can assert the existence of at least \(h\) distinct connected components isomorphic to \(t\). Indeed, quantify all vertices of each proposed finite component, specify every value of both unary functions on those vertices, close the component under both functions, and require disjointness of the listed vertex sets. Consequently every finite Boolean combination of events \(Z_t\ge h\) is attained as a first-order limiting probability, establishing the exact spectrum claimed.

**4. Density.** For the cycle types \(Q_k\), step 2 gives independent \(Z_{Q_k}\sim\operatorname{Poisson}(1/(2k))\). The sentence that a component belongs to any of finitely many types \(Q_k\) has limiting probability \(1-e^{-u_F}\), where \(u_F=\sum_{k\in F}(2k)^{-1}\). The terms tend to zero and their total sum diverges, so their finite subset sums are dense in \([0,\infty)\). Since \(u\mapsto1-e^{-u}\) continuously maps \([0,\infty)\) onto \([0,1)\), the attainable limiting probabilities are dense in \([0,1]\).

## Verification
The accompanying standalone Python 3 script `verify.py` enumerates every ordered pair of involutions on sets of sizes \(0\) through \(7\). It reconstructs each colored connected component, checks the generating-function coefficient formula and verifies \(63\) exact first, second and mixed factorial-moment identities with rational arithmetic. The check covers \(60{,}398\) ordered pairs of involutions and prints `TWO_INVOLUTION_COMPONENTS_EXACT_OK 60398 63 last_coefficient 3364/315` when all assertions pass. The computer calculation confirms finite identities only. The coefficient-ratio, Poisson and first-order statements are mathematical deductions proved above; no finite search establishes them.

## Relationship to prior work
Lugo [1], especially Sections 4 and 5, already established the colored path/cycle decomposition, the same generating function, and Poisson-type limits for the cycles of the composition of two random involutions. These are **not** new claims here. Puder and Zimhoni [2] establish much broader fixed-word cycle statistics for random actions of free products, again overlapping the probabilistic framework; their full openly available preprint was compared, including its statements on fixed-word cycles and asymptotic independence. The recent work of Marström and Räty [3] proves logical convergence for small permutation classes in the full two-order language, a different random-object model and signature. The new assessed statement is the **complete effective first-order probability spectrum of the two-involution relational structure, including its exact Poisson-threshold realization and density**. Its logical step uses classical bounded-degree Hanf locality [4], and novelty is not claimed for that theorem. A more general, previously established logical convergence theorem for assemblies might entail some of these conclusions; this remains a historical-priority limitation, not a proof of unique priority.

## Limitations
The result concerns only two independent uniformly sampled involutions with loops representing fixed points; it does not extend as stated to commuting involutions, involutions conditioned to be fixed-point-free, arbitrary group actions, or a language with an added global linear order. It proves first-order, not monadic second-order, convergence. The arithmetic characterization concerns each individual sentence's limiting probability and does not assert a uniform denominator across all sentences. The standard Hanf theorem gives a very large but computable reduction, with no practical complexity bound claimed. The finite checker is not an infinite proof. No independent scientific validation was performed. Priority remains subject to a more comprehensive survey of general logical limit-law theorems for combinatorial assemblies.

## References
[1] Michael Lugo, *The cycle structure of compositions of random involutions* (2009), arXiv:0911.3604, especially Theorem 4.1, Corollary 4.2, and Theorem 5.1, https://arxiv.org/abs/0911.3604.

[2] Doron Puder and Tomer Zimhoni, *Local Statistics of Random Permutations from Free Products* (2022 preprint; 2024 journal), arXiv:2203.12250, especially Theorems 1.13 and 1.14 and Section 6, https://arxiv.org/abs/2203.12250.

[3] Klas Marström and Eero Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages* (first public October 15, 2026), arXiv:2610.22218, https://arxiv.org/abs/2610.22218.

[4] Bounded-degree Hanf locality theorem, standard effective locality principle in finite model theory; see Leonid Libkin, *Elements of Finite Model Theory*, Springer (2004), Chapter 4.
