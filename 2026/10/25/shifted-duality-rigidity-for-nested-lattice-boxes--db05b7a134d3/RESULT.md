# Shifted-duality rigidity for nested lattice boxes

## Finding
Let \(d\ge1\), let \(a_1,\ldots,a_d\) be positive integers, and let \(b_1,\ldots,b_d\) be integers with \(0\le b_i\le a_i\). Define the axis-parallel lattice boxes
\[
P=\prod_{i=1}^d[0,a_i],\qquad Q=\prod_{i=1}^d[0,b_i].
\]
Write \(E_{P,Q}(t)\) for the number of integral translates of \(Q\) contained in \(tP\), and \(E^\circ_{P,Q}(t)\) for the number contained in the interior of \(tP\). **There exists a positive integer \(\sigma\) with \(E_{P,Q}(t)=E^\circ_{P,Q}(t+\sigma)\) for every sufficiently large integer \(t\) if and only if either all \(a_i=1\) or all \(a_i=2\).** The shift is necessarily unique: \(\sigma=2\) in the first case and \(\sigma=1\) in the second. In particular the answer is independent of all inner side lengths \(b_i\), including vanishing ones.

The nesting restriction is essential: without \(Q\subseteq P\), the noncubic pair \(P=[0,1]\times[0,3]\times[0,6]\), \(Q=[0,1]\times[0,4]\times[0,5]\) has shift \(\sigma=1\). For nonnested lattice boxes in dimension at most two, the only possible container side-length vectors remain \((1,\ldots,1)\) and \((2,\ldots,2)\).

## Assumptions and scope
The translations are by vectors in \(\mathbb Z^d\); boxes are aligned with the ambient integer coordinate lattice, not rotated. The outer box is full-dimensional; the inner box may be lower-dimensional. Interior means ordinary interior of the full-dimensional outer box. The shifted equality is an eventual equality of integer-valued functions, equivalently a polynomial identity. The theorem makes no claim about rational or real shifts or arbitrarily oriented parallelotopes.

## Proof
For sufficiently large integer \(t\), each coordinate of a permitted translating vector independently has exactly \(a_it-b_i+1\) choices for closed containment and \(a_it-b_i-1\) choices for strict containment. Consequently,
\[
E_{P,Q}(t)=\prod_{i=1}^d(a_it-b_i+1),\qquad
E^\circ_{P,Q}(t)=\prod_{i=1}^d(a_it-b_i-1).
\tag{1}
\]
These product formulas are known (Hirotsu, Example 2); we give the coordinate-count explanation to fix all boundary conventions.

Suppose the shifted equality holds with integer \(\sigma\ge1\). Divide the monic-normalized versions of both products in (1) by \(\prod_i a_i\). Their multisets of roots are, respectively,
\[
R=\left\{\frac{b_i-1}{a_i}:1\le i\le d\right\},\qquad
S=\left\{\frac{b_i+1}{a_i}-\sigma:1\le i\le d\right\},
\tag{2}
\]
with multiplicities. Polynomial equality forces \(R=S\). Equating sums of their elements gives
\[
d\sigma=2\sum_{i=1}^d\frac1{a_i},\qquad
\sigma=\frac2d\sum_{i=1}^d\frac1{a_i}.
\tag{3}
\]
Since \(a_i\ge1\), (3) gives \(0<\sigma\le2\). Thus \(\sigma\) is either \(1\) or \(2\).

If \(\sigma=2\), (3) forces the average of the numbers \(1/a_i\) to be one, hence every \(a_i=1\). Conversely, for these side lengths each factor of \(E^\circ_{P,Q}(t+2)\) equals the corresponding factor of \(E_{P,Q}(t)\).

Suppose \(\sigma=1\). If some \(a_j=1\), nesting makes \(b_j\in\{0,1\}\). When \(b_j=0\), the multiset \(R\) has the root \(-1\), whereas every element of \(S\) is strictly greater than \(-1\): indeed \((b_i+1)/a_i-1>-1\). When \(b_j=1\), the multiset \(S\) has the root \(1\), whereas every element of \(R\) is strictly less than \(1\) because \(b_i\le a_i\). Both cases contradict \(R=S\). Therefore every \(a_i\ge2\). Equation (3) now forces the average of \(1/a_i\le1/2\) to equal \(1/2\), so every \(a_i=2\). Conversely, with all \(a_i=2\) the factor identity \(2(t+1)-b_i-1=2t-b_i+1\) holds for every \(i\). This proves the classification and uniqueness.

For the nonnested witness, the two root multisets in (2), taking \(\sigma=1\), are both \(\{0,2/3,1\}\); hence their products agree. In dimensions one or two, equation (3) alone classifies any positive integral shift: for \(d=1\), it requires \(a_1\in\{1,2\}\); for \(d=2\), the case \(\sigma=1\) solves \(1/a_1+1/a_2=1\), equivalent to \((a_1-1)(a_2-1)=1\), hence \(a_1=a_2=2\), and \(\sigma=2\) forces both side lengths one. This establishes the sharp dimension-three contrast.

## Verification
The standalone standard-library script `proof_check.py` independently enumerates integer translations of small lattice boxes and tests the resulting exact integer counts against (1). It also performs exact rational multiset comparisons of the two polynomial root lists for every nested box with dimensions one through four and outer side lengths at most four. These finite checks confirm the formulas and boundary cases, but the preceding proof, rather than enumeration, establishes the statement for all dimensions. The nonnested example is checked as an exact polynomial identity.

## Relationship to prior work
Takashi Hirotsu introduced relative Ehrhart functions and the shifted-duality question in arXiv:2608.10370, first made public on 2026-08-11. Example 2 supplies formula (1); Theorem 7 addresses the different extended-inscription condition; and Problem 4 asks for a classification of pairs admitting shifted duality. This finding resolves that question **only for coordinatewise nested lattice boxes**, by proving rigidity independent of the inner box, rather than merely listing the familiar unit- and double-cube examples. The argument uses the published formulas as its starting point; it makes no claim that those formulas themselves are new. The nonnested witness illustrates why nesting cannot be dropped from the classification.

## Limitations
This is a classification within a structured subfamily of the general shifted-duality problem, not a solution for all convex lattice polytopes. The proof concerns integral positive shifts and lattice-aligned boxes, with exact integer coordinates. A complete historical-priority determination is not claimed; related arguments may exist under equivalent formulations of rational-root multisets or relative Ehrhart symmetry.

## References
1. T. Hirotsu, *Relative Ehrhart Functions: Eventual Polynomiality and Dualities*, arXiv:2608.10370v7 (2026), particularly Example 2, Definition 6, Theorem 7, and Problem 4. Public first version: 2026-08-11. https://arxiv.org/html/2608.10370v7
2. T. Hirotsu, *Normal-sized hypercuboids in a given hypercube*, arXiv:2211.15342 (2022), background on lattice-aligned hypercuboid counts. https://arxiv.org/abs/2211.15342
