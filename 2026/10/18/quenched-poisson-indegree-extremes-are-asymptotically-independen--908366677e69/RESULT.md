# Quenched Poisson indegree extremes are asymptotically independent of the complete random-mapping orbit

## Finding
Let \(f:[n]\to[n]\) be a uniformly random function, with its \(n\) values independent and uniform. Starting from \(v_0=1\), reveal \(v_{i+1}=f(v_i)\) up to the first repeat. Write \(T\in\{1,\ldots,n\}\) for the number of distinct encountered vertices, so that \(v_0,\ldots,v_{T-1}\) are distinct and \(v_T=v_J\) for a unique \(J\in\{0,\ldots,T-1\}\). The **complete labeled history** is \(H=(v_0,\ldots,v_T)\). Define \(N_{n,k}=\#\{v\in[n]:\deg_f^-(v)\ge k\}\) and \(b_{n,r}=\Pr\{\operatorname{Bin}(n,1/n)\ge r\}\).

**Theorem.** For every integer \(n\ge2\) and \(3\le k\le n\),
\[
d_{\mathrm{TV}}\bigl(\mathcal L(H,N_{n,k}),\mathcal L(H)\otimes\mathcal L(N_{n,k})\bigr)
\le 2\mathbb E[T]b_{n,k-1}+b_{n,k-2}
\le 2(1+\sqrt{\pi n/2})b_{n,k-1}+b_{n,k-2}.
\tag{1}
\]
Consequently, for each integer threshold sequence \(k=k_n\) satisfying
\[
n\Pr\{\operatorname{Poisson}(1)\ge k_n\}\longrightarrow\lambda\in(0,\infty),
\tag{2}
\]
the distance in (1) is \(O(k_n/\sqrt n)\). Moreover \(N_{n,k_n}\Rightarrow P\) for \(P\sim\operatorname{Poisson}(\lambda)\), and
\[
\left(\frac{J}{\sqrt n},\frac{T-J}{\sqrt n},N_{n,k_n}\right)
\Rightarrow(A,B,P),
\tag{3}
\]
where \(P\) is independent of \((A,B)\) and \((A,B)\) has joint density
\[
(a,b)\longmapsto e^{-(a+b)^2/2}\,\mathbf1_{\{a\ge0,b\ge0\}}.
\tag{4}
\]
In particular, the event that **no vertex has indegree at least** \(k_n\) has limiting probability \(e^{-\lambda}\), jointly independent of the limiting orbit-tail and orbit-cycle lengths.

## Assumptions and scope
All randomness is the independent uniform map model, **not** a random map with a prescribed indegree sequence. Total variation means the supremum of probability differences over events; the random labeled history is retained in full, and the product comparison is made separately for each finite \(n\). The threshold \(k_n\) is integer-valued, and (2) concerns sequences or subsequences where the Poisson-tail mean converges to a nonzero finite value. Such sequences exist but are not asserted to include every integer \(n\) for one fixed \(\lambda\), because the threshold is lattice-valued. The primary classification is 60C05.

## Proof
**Step 1 (exposure and a sharp conditional coupling).** Fix an admissible entire labeled orbit history \(h=(v_0,\ldots,v_m)\) with \(v_m=v_j\). The \(m\) outputs at domains \(v_0,\ldots,v_{m-1}\) are prescribed, and all other \(n-m\) map outputs remain independent uniform destinations. Coupled to this conditional random function, let \(Z\) be the number of bins having at least \(k\) occupants **from the unexposed \(n-m\) outputs alone**. Among the \(m\) prescribed destinations, at most one vertex receives two arrows (this occurs only if \(j\ge1\)); every other prescribed destination receives at most one arrow. An individual bin has at least \(k-1\) unexposed occupants with probability at most \(b_{n,k-1}\), while the potentially doubled bin has at least \(k-2\) with probability at most \(b_{n,k-2}\). A union bound therefore gives
\[
\Pr\{N_{n,k}\ne Z\mid H=h\}\le m b_{n,k-1}+b_{n,k-2}.
\tag{5}
\]

Independently append \(m\) new uniform destinations to those same unexposed \(n-m\) outputs. Counting bins of occupancy at least \(k\) after this completion produces a variable \(N'\) with **exactly** the unconditional distribution of \(N_{n,k}\). Any crossing of threshold \(k\) created by these additional balls must occur when a new ball lands in a bin already containing at least \(k-1\) balls. Before each new arrival the occupancy of a fixed target bin is stochastically dominated by \(\operatorname{Bin}(n,1/n)\), hence
\[
\Pr\{N'\ne Z\mid H=h\}\le m b_{n,k-1}.
\tag{6}
\]
Combining (5) and (6) proves the pointwise bound
\[
d_{\mathrm{TV}}\bigl(\mathcal L(N_{n,k}\mid H=h),\mathcal L(N_{n,k})\bigr)
\le2m b_{n,k-1}+b_{n,k-2}.
\tag{7}
\]
Averaging over histories proves the first inequality in (1). No assumption of independence of the revealed arrows is made; it is the **remaining** map outputs that are independent after conditioning.

**Step 2 (the orbit-length expectation).** For \(0\le t\le n-1\),
\[
\Pr\{T>t\}=\prod_{i=1}^{t}\left(1-\frac{i}{n}\right)
\le \exp\left(-\frac{t(t+1)}{2n}\right).
\tag{8}
\]
Summation of the tail, bounded by a decreasing Gaussian integral, yields
\[
\mathbb E[T]\le1+\sqrt{\pi n/2}.
\tag{9}
\]
The exact probability of \(T=m,J=j\) is \((n-1)_{m-1}/n^m\), the same for every \(0\le j<m\), where \((n-1)_{m-1}\) is a falling factorial. In particular \(J\mid T=m\) is uniform on \(\{0,\ldots,m-1\}\).

**Step 3 (rare-threshold scale).** Assume (2). Standard successive-tail ratio estimates for Poisson(1) imply \(k_n\to\infty\), \(k_n\sim\log n/\log\log n\), and for each fixed \(r\ge0\), the ratio of the tail at \(k_n-r\) to the tail at \(k_n\) has order \(k_n^r\). For \(k_n=O(\log n)\), the binomial probability at occupancy \(t=O(k_n)\), divided by the corresponding Poisson(1) mass, converges uniformly to \(1\): explicitly the ratio is
\[
e\frac{(n)_t}{n^t}\left(1-\frac1n\right)^{n-t}=1+o(1).
\tag{10}
\]
Contributions from occupancies greater than \(2k_n\) are negligible relative to the tail at \(k_n-r\). It follows that
\[
b_{n,k_n-1}=O(k_n/n),\qquad b_{n,k_n-2}=O(k_n^2/n).
\tag{11}
\]
Insert (9) and (11) into (1) to obtain \(O(k_n/\sqrt n)\), since \(k_n=o(\sqrt n)\).

**Step 4 (rare indegrees are Poisson).** For fixed integer \(q\ge1\) and nonnegative occupancies \(t_1,\ldots,t_q\) with sum \(s\le n\), the joint multinomial distribution of the occupancies of \(q\) specified vertices, divided by the law of \(q\) independent Poisson(1) variables, equals
\[
R_{n,q}(t_1,\ldots,t_q)=e^q\frac{(n)_s}{n^s}\left(1-\frac qn\right)^{n-s}.
\tag{12}
\]
This ratio is bounded by \(e^q\) whenever \(q\le n\), and it tends uniformly to \(1\) when every \(t_i=k_n+O(1)\), because \(k_n^2/n\to0\). Conditional on independent Poisson(1) variables each being at least \(k_n\), they equal \(k_n+O_{\Pr}(1)\); in fact their excesses vanish in probability. Dominated convergence applied to (12) gives
\[
\Pr\{\deg_f^-(v_i)\ge k_n\ \forall i\le q\}
\sim\bigl[\Pr\{\operatorname{Poisson}(1)\ge k_n\}\bigr]^q.
\tag{13}
\]
The \(q\)-th factorial moment of \(N_{n,k_n}\) consequently converges to \(\lambda^q\) for every fixed \(q\), proving its Poisson limit.

**Step 5 (joint orbit and indegree extremes).** By (8), \(T/\sqrt n\) converges to a Rayleigh variable \(R\) with survival \(\Pr\{R>s\}=e^{-s^2/2}\) for \(s\ge0\). Since \(J\mid T=m\) is discrete uniform, \((J/\sqrt n,(T-J)/\sqrt n)\Rightarrow(UR,(1-U)R)\), where \(U\sim\operatorname{Uniform}[0,1]\) is independent of \(R\). A change of coordinates yields the density (4). Finally, total-variation convergence of the **full history** product law in (1) supplies asymptotic independence of any functions of the history, including the two orbit lengths, from \(N_{n,k_n}\). This proves (3) and its maximum-indegree consequence.

## Verification
Run `python verify_mapping.py` using Python's standard library. The independent finite checker enumerates all \(n^n\) functions for each \(2\le n\le6\) (50,068 maps), checks exact orbit-history probabilities, computes the exact conditional high-indegree count law for every admissible pair of orbit lengths and repetition indices, and verifies (7) using rational arithmetic. Its recorded output is `VERIFY_OK mappings 50068 conditionals 210 assertions 802`. These tests validate finite identities and boundary behavior, not the infinite limiting assertions; those follow from the five analytical steps above.

## Relationship to prior work
Hansen and Jaworski (2008, first publicly available online in 2007) investigate exchangeable-indegree random mappings, including cyclic points, components and local successor/predecessor distributions. Their local-property paper gives joint local exploration distributions, but the material inspected does not state a total-variation product estimate for the **entire labeled orbit** versus the **number of globally exceptional indegrees**. Perkins's *The Forgetfulness of Balls and Bins* studies total variation for globally planted occupancy allocations, an importantly related but differently quantified question: the present estimate projects to a rare threshold-count statistic and applies after a random birthday-length exploration, a regime not immediately furnished by the global-configuration theorem. Arratia, Garibaldi and Kilian analyze multiple-collision birthday stopping times rather than high-indegree extremes coupled to a mapping orbit. Earlier random-mapping surveys and an inaccessible original monograph/article can still contain an implicit stronger statement; priority is not certified by keyword or database searches.

## Limitations
The result is specific to independent uniform map outputs and high **indegree threshold counts**, not the full in-degree vector, for which such independence would be false after revealing the history. The bound is informative only when its right-hand side is small and does not assert any uniform local limit at thresholds without a convergent rare-event parameter. The lattice restriction in (2) is essential. Finite enumeration is not a proof of the asymptotic statement. Historical priority, particularly possible implicit coverage by Flajolet and Odlyzko's 1990 broad random-mapping survey, requires independent specialist scrutiny: lawful full-text access to that survey could not be completed.

## References
1. J. C. Hansen and J. Jaworski, *Random mappings with exchangeable in-degrees*, Random Structures & Algorithms 33 (2008), 105–126, first published online 2007-09-04, DOI: 10.1002/rsa.20187.
2. J. C. Hansen and J. Jaworski, *Local properties of random mappings with exchangeable in-degrees*, Advances in Applied Probability 40 (2008), 183–205, DOI: 10.1017/S0001867800002433; author/hosted full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6993B104668C73703B9E57AF3DCC643E/S0001867800002433a.pdf/local-properties-of-random-mappings-with-exchangeable-indegrees.pdf .
3. W. Perkins, *The Forgetfulness of Balls and Bins*, arXiv:1004.5373, first submitted 2010-04-29.
4. R. Arratia, S. Garibaldi and J. Kilian, *Asymptotic distribution for the birthday problem with multiple coincidences, via an embedding of the collision process*, arXiv:1310.7055, first submitted 2013-10-26.
5. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, Advances in Cryptology—EUROCRYPT '89 (1990), broadly relevant survey; full-text priority comparison incomplete.
