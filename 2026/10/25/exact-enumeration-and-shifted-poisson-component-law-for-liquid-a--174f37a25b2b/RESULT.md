# Exact enumeration and shifted-Poisson component law for liquid approval profiles

## Finding
Let \(V=[n]\) be a labeled set of peers, and let \(f:V\to V\) be a total delegation function. Write \(A_f(i)=\{f^t(i):t\ge1\}\) for peer \(i\)'s approval set. Two functions give the same *liquid approval profile* when all their approval sets coincide, with the labels fixed. For \(n\ge1\), denote by \(P_n\) the number of distinct liquid profiles, by \(C_n\) the number with one weak delegation component, and by \(P_{n,j}\) the number with exactly \(j\) components.

**Theorem.** Define the rooted labeled-tree series
\[
T(z)=\sum_{m\ge1}\frac{m^{m-1}}{m!}z^m,\qquad T(z)=z\exp(T(z)).
\]
Then the exact bivariate exponential generating function is
\[
\boxed{\sum_{n,j\ge0}P_{n,j}u^j\frac{z^n}{n!}
=\exp\!\left(u(e^z-1)e^{T(z)}\right).}
\]
In particular, for \(n\ge1\),
\[
\boxed{C_n=\sum_{s=1}^n\binom ns(n-s+1)^{n-s-1},}
\]
where the summand at \(s=n\) is understood to equal one. The first six values of \(C_n\) are \(1,3,13,87,821,10023\); those of \(P_n\) are \(1,4,23,185,1942,25315\).

For any given liquid profile, let its distinct sink-cycle sets have sizes \(s_1,\ldots,s_j\); let \(b_a\) count the non-sink vertices immediately below sink set \(a\) in the canonical contracted rooted forest. The number of delegation functions inducing precisely that **labeled** profile is
\[
\boxed{\#\{f:A_f=A\}=\prod_{a=1}^j(s_a-1)!\,s_a^{b_a}.}
\]

Let \(\rho=e^{-1}\) and \(a=e(e^{1/e}-1)\). For fixed real \(u>0\) (uniformly for complex \(u\) near one),
\[
\sum_{j\ge0}P_{n,j}u^j\sim ua e^{ua}n^{n-1},
\qquad P_n\sim ae^a n^{n-1}.
\]
If \(K_n\) is the number of components in a uniformly selected **distinct labeled liquid profile**, then
\[
\boxed{K_n\ \xrightarrow{d}\ 1+\operatorname{Poisson}(a),}
\qquad \frac{C_n}{P_n}\longrightarrow e^{-a}\approx0.29857546.
\]
Under a different sampling convention—one uniformly chosen total delegation function among \(n^n\) functions—the probability of one connected component is instead
\[
\boxed{\mathbb P_{f\text{ uniform}}(\text{one component})
\sim\sqrt{\frac{\pi}{2n}}\longrightarrow0.}
\]
Thus the two natural ways of sampling this voting domain produce qualitatively different component statistics.

## Assumptions and scope
All peers are individually labeled; every peer chooses **exactly one** delegate, potentially themselves; approval is positive-length directed reachability. Every labeled approval matrix is counted once, regardless of how many delegation functions witness it. A component is the weakly connected component of any witnessing function (it is intrinsically identified by overlapping reachability sets). No assumption is made about committee size, voting weights, or approval-rule outcomes. The formulas concern finite \(n\ge1\); an empty profile of size zero is assigned one formal counting object for the generating function.

## Proof
**1. Canonical shape and fiber multiplicity.** A finite functional graph has in each weak component exactly one terminal directed cycle \(S\), possibly a self-loop; all other vertices form trees directed toward it. Since reachability is by positive-length paths, a vertex approves itself if and only if it belongs to this cycle. Therefore \(S\), and the partition into components (by sharing a terminal approved vertex), are intrinsic to the approval profile. Every noncyclic vertex \(v\) has a uniquely determined ordered list of noncyclic successors, from its approval set: its first such successor \(w\), if one exists, is the unique noncyclic element of \(A(v)\) satisfying \(|A(w)|=|A(v)|-1\). If none exists, \(v\) points directly into \(S\). After contracting \(S\) to a single abstract root, the remaining vertices therefore form a uniquely recovered directed labeled tree, rooted at that abstract vertex. Conversely, choosing any nonempty labeled sink set and such a rooted tree defines one approval profile: a cycle vertex approves all of \(S\), and any outside vertex approves \(S\) plus the outside vertices on its directed path to the contracted root. This proves a bijection at the level of **profiles**, not merely witnessing graphs.

For a fixed recovered structure, each sink set of size \(s\) admits precisely \((s-1)!\) directed cyclic orderings. Each of its \(b\) direct children independently chooses any of the \(s\) cycle vertices as delegate. Every remaining arrow is already forced by the recovered rooted tree. The stated product counts all and only functions with that labeled profile.

**2. Exact enumeration.** For a connected component on \(n\) labels, choose a nonempty sink subset of size \(s\), and then a labeled tree on the other \(n-s\) labels plus one prescribed abstract root. Cayley's formula gives \((n-s+1)^{n-s-1}\) such trees, interpreted as one for \(s=n\). Summing over the sink subsets yields the displayed \(C_n\).

The rooted labeled-tree exponential generating function \(T(z)\) satisfies \(T=ze^T\). A connected profile is one nonempty **set** of labels belonging to the sink, together with a **set** of rooted labeled trees hanging immediately beneath the contracted sink, hence its EGF is
\[
C(z)=(e^z-1)\exp(T(z)).
\]
Every profile is an unordered **set** of nonempty connected profiles on disjoint label sets. Marking each component by \(u\), the labeled exponential formula gives the claimed \(\exp(uC(z))\). Equivalently, the exact recurrence is \(P_0=1\) and
\[
P_n=\sum_{k=1}^n\binom{n-1}{k-1}C_kP_{n-k}.
\]

**3. Profile asymptotics and component law.** The tree function has its unique dominant positive singularity at \(\rho=e^{-1}\), where \(T(\rho)=1\). Its standard square-root expansion in a dented analytic neighborhood of \(\rho\) is
\[
T(z)=1-\sqrt{2(1-ez)}+O(1-ez).
\]
Writing \(a=(e^\rho-1)e\), it follows that
\[
C(z)=a-a\sqrt{2(1-ez)}+O(1-ez).
\]
Consequently, uniformly for \(u\) near one,
\[
\exp(uC(z))=e^{ua}-ua\sqrt2 e^{ua}\sqrt{1-ez}+O(1-ez).
\]
Standard square-root singularity transfer yields
\[
[z^n]\exp(uC(z))\sim\frac{ua e^{ua}e^n}{\sqrt{2\pi}\,n^{3/2}}.
\]
Multiplication by \(n!\sim\sqrt{2\pi n}(n/e)^n\) proves the uniform asymptotic formula. Dividing by the case \(u=1\) shows that the probability generating functions of \(K_n\) converge to \(u\exp(a(u-1))\), that of one plus a Poisson random variable with mean \(a\). Taking \(u=1\) in \(C_n\sim a n^{n-1}\) and comparing with \(P_n\) establishes the connected fraction.

**4. Uniform delegation functions.** Standard directed-cycle decomposition of labeled mappings gives the EGF
\[
M(z)=\frac1{1-T(z)},\qquad \log M(z)=-\log(1-T(z))
\]
for all maps and for connected maps, respectively. By the square-root expansion, \(-\log(1-T(z))=-\tfrac12\log(1-ez)+O(1)\) with the remaining singular term of order \(\sqrt{1-ez}\). Thus the number of connected labeled mappings is asymptotic to \(n!e^n/(2n)\). Dividing by the exact \(n^n\) total mappings and using Stirling proves the final formula.

## Verification
The standalone `check_liquid_profiles.py` enumerates every map on labeled sets with one through six vertices, constructs its exact reachability profile, aggregates fiber multiplicities, checks the claimed product for each fiber, and independently compares the distinct and connected counts against Cayley's formula and the EGF recurrence. Its exact output is: connected counts \(1,3,13,87,821,10023\), profile counts \(1,4,23,185,1942,25315\), and 1, 4, 27, 256, 3125, 46656 maps considered, respectively. It also checks finite-\(n\) numerical trends against the proved asymptotics. Run with a standard Python 3 interpreter; no third-party modules or external data are required. These finite checks do not prove the asymptotic or general-\(n\) assertions; those follow from the bijection and analytic arguments above.

## Relationship to prior work
Grossi, Lisowski, and Papasotiropoulos (2026) introduce liquid approval profiles for peer selection and establish structural and computational properties, including a recognition procedure. The present statement addresses a different quantitative question: exact **numbers of distinct labeled profiles**, sizes of fibers of the delegation-to-approval map, and the component distribution under two different sampling spaces. Classical functional-digraph decomposition, Cayley's tree enumeration, and singularity analysis are used as prior mathematical tools. Aho, Garey, and Ullman's transitive reduction theory analyzes equivalent reachability representations generally, rather than the resulting enumerative and sampling formulas for this approval domain. Harary's classical functional-digraph enumeration concerns underlying digraphs; it does not by itself identify the quotient by labeled approval equality. These classical ingredients are not claimed as new.

## Limitations
This result assumes out-degree exactly one, allows loops and cycles, and identifies approval profiles that share all positive-length reachability sets on a fixed labeled set. It does not count unlabeled isomorphism classes, analyze committee outcomes, or characterize larger multi-delegation systems. The uniform-profile probability model assigns equal weight to distinct approval matrices; it is not a behavioral model of actual delegation choices. Priority relative to differently named earlier combinatorial enumerations remains subject to future independent literature verification.

## References
1. Davide Grossi, Grzegorz Lisowski, Georgios Papasotiropoulos, *Representation in Peer Selection: A Liquid Democracy Perspective*, arXiv:2608.13085 (first posted 13 August 2026), https://arxiv.org/abs/2608.13085.
2. Alfred V. Aho, Michael R. Garey, Jeffrey D. Ullman, *The Transitive Reduction of a Directed Graph*, SIAM Journal on Computing **1** (1972), 131–137, doi:10.1137/0201008.
3. Frank Harary, *The Number of Functional Digraphs*, Mathematische Annalen **138** (1959), 203–210, doi:10.1007/BF01342903.
4. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), chapters II, VI, VII (labeled constructions, singularity transfer, functional graphs).
