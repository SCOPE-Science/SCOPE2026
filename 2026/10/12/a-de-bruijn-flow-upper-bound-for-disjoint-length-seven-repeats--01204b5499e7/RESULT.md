# A de Bruijn-flow upper bound for disjoint length-seven repeats
## Finding
Let \(C(k,n)\) denote the maximum length of a word over a \(k\)-letter alphabet with no two disjoint occurrences of the same length-\(n\) factor.

For each \(w\in\Sigma_k^n\), write \(\operatorname{per}(w)\) for its least period and define the capacity
\[
c(w)=\left\lceil\frac{n}{\operatorname{per}(w)}\right\rceil.
\]
Consider the order-\((n-1)\) de Bruijn digraph: its vertices are \(\Sigma_k^{n-1}\), and the edge indexed by \(w=w_1\cdots w_n\) goes from \(w_1\cdots w_{n-1}\) to \(w_2\cdots w_n\).

Let \(F(k,n)\) be the maximum of
\[
\sum_{w\in\Sigma_k^n}x_w
\]
over all real edge vectors satisfying
\[
0\le x_w\le c(w)
\]
and whose directed incidence vector is either \(0\) or \(e_s-e_t\) for two distinct vertices \(s,t\). Then
\[
C(k,n)\le F(k,n)+n-1.
\]

For \(k=2\) and \(n=7\), the exact value of this relaxation is
\[
F(2,7)=220.
\]
Therefore
\[
C(2,7)\le226.
\]

The earlier counting bound obtained by summing the capacities independently gives \(242\) in this case, while the published construction gives \(C(2,7)\ge192\). Thus the new flow constraint lowers the published upper bound by \(16\) and reduces the unresolved interval from width \(50\) to width \(34\).

## Assumptions and scope
Two occurrences of a length-\(n\) factor are disjoint when their intervals of positions do not intersect. The parameter \(C(k,n)\) is exactly the one defined by Gabrić, Shallit, and Zhong.

The proof uses their lemma that if a length-\(n\) factor \(w\) occurs in a word without two disjoint occurrences, then the number of its occurrences is at most
\[
\left\lceil\frac{n}{\operatorname{per}(w)}\right\rceil.
\]
The new ingredient is to retain the overlap consistency among consecutive length-\(n\) factors instead of summing these per-factor capacities independently.

The numerical conclusion concerns \(C(2,7)\). The general flow inequality applies to every \(k\ge1\) and \(n\ge1\), but no claim is made here that the flow relaxation is exact for \(C(k,n)\).

## Proof
Let \(W\) be a word of length \(L\ge n\) with no two disjoint occurrences of the same length-\(n\) factor. Reading the \(L-n+1\) consecutive length-\(n\) factors of \(W\) gives a directed walk in the order-\((n-1)\) de Bruijn digraph. Let \(x_w\) be the number of times this walk traverses edge \(w\).

By the occurrence bound quoted above,
\[
0\le x_w\le c(w)
\]
for every edge \(w\).

Every finite directed walk has balanced edge multiplicities at all internal vertices. If its initial and terminal \((n-1)\)-factors coincide, its incidence vector is \(0\). Otherwise its incidence vector is \(e_s-e_t\), where \(s\) is the initial vertex and \(t\) the terminal vertex. Hence \(x\) is feasible for the definition of \(F(k,n)\). Therefore
\[
L-n+1=\sum_w x_w\le F(k,n),
\]
which proves
\[
C(k,n)\le F(k,n)+n-1.
\]

It remains to evaluate the binary \(n=7\) relaxation. There are \(64\) vertices and \(128\) edges. The sum of the independent capacities is
\[
\sum_{w\in\{0,1\}^7}c(w)=236.
\]
Write \(u\) for this full-capacity edge vector and \(B\) for the directed incidence matrix. A feasible retained vector has the form \(x=u-d\). For a prescribed walk incidence \(b\), where \(b=0\) or \(b=e_s-e_t\), the deleted vector \(d\) must satisfy
\[
Bd=Bu-b,\qquad 0\le d\le u.
\]
Thus maximizing retained capacity is equivalent to minimizing \(\sum_w d_w\).

The bundled certificate supplies an integer dual potential for every one of the \(1+64\cdot63=4033\) possible incidence choices. For a required deletion imbalance \(h=Bu-b\) and a potential \(\pi\), weak duality gives
\[
\sum_w d_w\ge
\pi\mathbin{\cdot}h+
\sum_{w=(p,q)}
u_w\min\!\left(0,\,1-\pi_p+\pi_q\right).
\]
Every certified right-hand side is at least \(16\). Hence every feasible retained vector uses at most
\[
236-16=220
\]
edges.

The certificate also gives a feasible deleted vector of total multiplicity \(16\) for one endpoint pair. Consequently the relaxation optimum is exactly \(220\), and
\[
C(2,7)\le220+6=226.
\]

## Verification
Run `python3 verify.py` in the package directory.

The verifier independently reconstructs all \(128\) binary length-\(7\) factors, computes their least periods and capacities, checks the total capacity \(236\), and reconstructs the order-\(6\) de Bruijn incidence matrix.

It then checks that the certificate contains exactly the closed-walk case and all \(64\cdot63\) ordered distinct endpoint pairs. For every case it evaluates the displayed dual lower bound using integer arithmetic and verifies that at least \(16\) units of capacity must be deleted. Finally it checks the bundled feasible deletion vector of size \(16\). These two checks establish the exact relaxation value \(220\) without floating-point optimization.

## Relationship to prior work
Gabrić, Shallit, and Zhong introduced \(C(k,n)\), proved the per-factor occurrence bound used above, and obtained
\[
C(k,n)\le
\sum_{w\in\Sigma_k^n}
\left\lceil\frac{n}{\operatorname{per}(w)}\right\rceil+n-1.
\]
They computed \(C(2,n)\) exactly through \(n=6\), and reported only
\[
C(2,7)\ge192.
\]
For \(n=7\), their general counting inequality evaluates to \(242\). Their concluding remarks explicitly identify improvements of this upper bound and additional values of \(C(k,n)\) as open computational directions.

The flow inequality is not a restatement of that counting bound: it additionally enforces the de Bruijn incidence balance forced by consecutive overlapping windows. Targeted searches under the exact parameter \(C(2,7)\), disjoint-occurrence terminology, de Bruijn-flow terminology, and equivalent capacity-walk formulations did not locate a published bound of \(226\) or stronger for this parameter. Later citations located for the source concern overlap avoidance in two-dimensional pictures rather than the one-dimensional \(C(k,n)\) extremal function.

## Limitations
The result does not determine \(C(2,7)\); the published lower bound \(192\) remains separated from the new upper bound \(226\).

The flow model is a relaxation. Incidence balance and per-edge capacities are necessary for a factor sequence to come from an admissible word, but they do not encode the full positional requirement that repeated occurrences of one factor must overlap pairwise. Accordingly, equality in the flow relaxation need not correspond to an actual word.

The originality search cannot exclude an unindexed computation or an unpublished improvement of the same bound.

## References
1. D. Gabrić, J. Shallit, and X. F. Zhong, “Avoidance of split overlaps,” arXiv:2002.01968, first public version 2020-02-05; Discrete Mathematics 344 (2021), 112176, DOI 10.1016/j.disc.2020.112176.
