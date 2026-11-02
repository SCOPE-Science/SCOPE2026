# Support-refined census of optimal total \(\{k\}\)-dominating functions on cycles

## Finding
Let \(n\ge3\) and \(k\ge2\) be integers. On the labelled simple cycle \(C_n\) with vertex set \(\mathbb Z/n\mathbb Z\), call \(f:V(C_n)\to\{0,1,\dots,k\}\) a total \(\{k\}\)-dominating function when
\[
f(i-1)+f(i+1)\ge k\qquad(i\in\mathbb Z/n\mathbb Z).
\]
Let \(\mathcal M_{n,k}\) be the family of such functions with minimum weight \(\sum_i f(i)\), and let their **support enumerator** be
\[
S_{n,k}(u)=\sum_{f\in\mathcal M_{n,k}}u^{|\{i:f(i)>0\}|}.
\]
Then the complete support-refined optimal census is
\[
\boxed{S_{n,k}(u)=
\begin{cases}
4u^{n/2}+4(k-1)u^{3n/4}+(k-1)^2u^n,&n\equiv0\pmod4,\\
(n/2)^2u^n,&n\equiv2\pmod4,\ k\text{ odd},\\
u^n,&\text{otherwise}.
\end{cases}}
\]
The previously determined minimum weight is \(kn/2\), except that it is \(kn/2+1\) when \(n\equiv2\pmod4\) and \(k\) is odd, and is \(\lceil kn/2\rceil\) when \(n\) is odd. In particular the **number** of optimum functions is \((k+1)^2\) when \(4\mid n\), is \((n/2)^2\) when \(n\equiv2\pmod4\) and \(k\) is odd, is \(n\) when \(n\) and \(k\) are both odd, and is \(1\) otherwise.

A structural consequence not visible from the optimum weight alone is the exact support phase transition:
\[
\boxed{\exists f\in\mathcal M_{n,k}:\ f(i)=0\text{ for some }i\quad\Longleftrightarrow\quad 4\mid n.}
\]
When \(4\mid n\), exactly four optimum functions have minimum support size \(n/2\); their positive labels are all \(k\). For all other lengths, **every** optimal function is strictly positive at every vertex.

## Assumptions and scope
Cycles are simple, undirected, and carry fixed vertex labels; functions are counted individually, without quotienting by dihedral automorphisms. The parameter \(k\) is an integer at least two and labels are integers from zero to \(k\), not real weights or binary \(k\)-tuple selections. The term support means the vertices carrying strictly positive labels. The minimum-weight value is known from Tan, Liu and Liang (2018); the new assertion is the complete structural and support-refined census of **all** optimal functions for \(k\ge2\).

## Proof
Introduce the *step-two constraint graph* on vertex labels: one constraint \(f(i-1)+f(i+1)\ge k\) for each \(i\), so its edges link indices differing by two. If \(n\) is odd, this is one cycle of length \(n\). If \(n\) is even, it is two separate cyclic chains of length \(m=n/2\), one on the even indices and one on the odd indices. For \(n=4\), each two-vertex chain has its edge constraint repeated; repetitions do not affect feasibility or optimality. Thus the problem is a sum of independent copies of the following integer covering problem on a cyclic chain.

**Cyclic-chain lemma.** Let \(m\ge2\), \(k\ge1\) and \(x_0,\dots,x_{m-1}\in\{0,\dots,k\}\) satisfy \(x_j+x_{j+1}\ge k\), indices taken cyclically. If \(m\) is even, the minimum sum is \(mk/2\) and its **complete set** of minimizers consists of the \(k+1\) alternating assignments \(a,k-a,a,k-a,\dots\) with \(a\in\{0,\dots,k\}\). If \(m\) is odd and \(k\) is even, the minimum is \(mk/2\), achieved uniquely by the constant assignment \(k/2\). If both \(m\) and \(k\) are odd, the minimum is \((mk+1)/2\); there are exactly \(m\) minimizers, all labelled by a unique edge with sum \(k+1\) while all other edge sums are \(k\), and all labels are either \((k-1)/2\) or \((k+1)/2\).

To prove the lemma, summing the \(m\) edge constraints gives \(2\sum_j x_j\ge mk\). When the right side is even, equality of total weight forces every edge constraint to be equality. The equations \(x_{j+1}=k-x_j\) alternate; they have \(k+1\) solutions when \(m\) is even, but for odd \(m\) force \(x_j=k/2\) for every \(j\), possible only for even \(k\). If \(m,k\) are both odd, integer weights require sum at least \((mk+1)/2\), and any solution of that weight has total edge slack \(\sum_j(x_j+x_{j+1}-k)=1\). There is therefore exactly one slack edge, with slack one. Choosing its position and alternating the other equality equations uniquely gives the two labels \((k\pm1)/2\), with the high label on both endpoints of that slack edge. Conversely that assignment satisfies all constraints, and each of the \(m\) possible slack edges yields a distinct minimizer. This proves the lemma, including its equality classification; no finite search is involved.

If \(n\) is odd, the step-two constraint graph is a single odd chain. The lemma gives a unique constant optimum when \(k\) is even or \(n\) distinct optimum assignments when \(k\) is odd. Since \(k\ge2\), every label appearing in either case is positive. This gives \(S_{n,k}(u)=u^n\) for even \(k\), and \(S_{n,k}(u)=nu^n\) for odd \(k\).

If \(n\equiv2\pmod4\), the two independent step-two chains both have odd length \(m=n/2\). For even \(k\), each has one constant minimizer; for odd \(k\), each has exactly \(m\) minimizers. Because the total weight is the sum of the two independent chain weights, every global minimizer chooses a minimizer of **each** chain, and conversely. Their total numbers are therefore one and \(m^2\), respectively. All labels are positive when \(k\ge2\), yielding the stated full-support monomials.

If \(4\mid n\), the two step-two chains both have even length \(m=n/2\). For each chain independently choose \(a\in\{0,\dots,k\}\) and alternate \(a,k-a\). Both halves then carry exactly \(mk/2\) weight, so there are \((k+1)^2\) global minima. On each chain, a boundary choice \(a=0\) or \(a=k\) produces exactly \(m/2=n/4\) zero labels; each of the \(k-1\) interior choices produces none. Across the two chains: two boundary choices give \(4\) functions with support \(n/2\); exactly one boundary gives \(4(k-1)\) with support \(3n/4\); two interior choices give \((k-1)^2\) with support \(n\). These cases exhaust all minimizers and prove the displayed polynomial and the support criterion.

## Verification
The accompanying standalone `verify.py` implements two independent finite checks directly from the original neighbor inequalities. It enumerates every function of allowable labels for \(3\le n\le8\), \(1\le k\le3\), checking optimum weight, number, and for \(k\ge2\) each support coefficient. A second dynamic program enforces the untransformed cyclic neighborhood inequalities and verifies optimum weight and multiplicity for \(3\le n\le30\), \(1\le k\le4\). Its successful run reports `ORIGINAL_NEIGHBORHOOD_EXHAUSTIVE_OK 18`, `INDEPENDENT_CYCLIC_DYNAMIC_PROGRAM_OK 112`, and `VERIFY_OK`. These are consistency checks, not proofs for unbounded parameters; the preceding argument proves all quantified cases.

## Relationship to prior work
Tan, Liu and Liang (2018), Theorem 2.1, determined the minimum *weight* of a total \(\{k\}\)-dominating function on cycles and exhibited optimum examples. Their argument includes the same summation lower bound, but does not state an enumeration of **all** optimal functions or a support-refined polynomial. Escalante, Tolomei and Lopez Pujato (arXiv posted 2026-10-19) motivated a current broader study of total \(\{k\}\)-domination, with new exact structures for weighted total domination on caterpillars. OEIS A302653 already records the numbers of minimum ordinary total-dominating **sets**, corresponding to \(k=1\); the present enumerative and support statement is deliberately restricted to \(k\ge2\), where optimal functions can take more than two distinct values. This theorem does not claim the earlier minimum-weight result or the \(k=1\) count as new.

## Limitations
No claim is made for arbitrary graphs, for paths, or for classifications modulo graph automorphisms. The proof is elementary, and the historically published minimum-weight calculation provides the starting point; mathematical priority for the new all-optima/support refinement has not been independently audited. All claims count explicitly labelled functions. No independent external mathematical audit has been performed.

## References
- H. Tan, L. Liu, H. Liang, "Total {k}-Domination in Special Graphs," *Mathematical Foundations of Computing* 1(3) (2018), 255–263, doi:10.3934/mfc.2018011; Theorem 2.1.
- M. Escalante, P. Tolomei, M. I. Lopez Pujato, "Total {k}-domination in caterpillars: Structural properties and exact results," arXiv:2610.27181, first posted 2026-10-19.
- OEIS A302653, "Number of minimum total dominating sets in the n-cycle graph," https://oeis.org/A302653 (preexisting \(k=1\) values).
