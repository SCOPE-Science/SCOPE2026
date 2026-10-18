# Exact projective Fourier-support diagram for nonnegative ray-invariant functions

## Finding
Let \(q\ge2\) be a prime power, \(G=\mathbb F_q^2\), and \(f:G\to[0,\infty)\) be nonzero and invariant under multiplication of its argument by \(\mathbb F_q^\times\). The punctured one-dimensional subspaces of \(G\) are called rays; they form \(n=q+1\) projective directions. Let \(\varepsilon\in\{0,1\}\) indicate whether \(f(0)>0\), and let \(s\) count rays carrying positive values. Let \(r\) count dual rays carrying nonzero Fourier values. The Fourier transform is unnormalized. Its origin value is strictly positive, so
\[
|\operatorname{supp}f|=\varepsilon+(q-1)s,\qquad
|\operatorname{supp}\widehat f|=1+(q-1)r.
\]
All and only the following triples are attainable:

* \(\varepsilon=1,s=0:\ r=n\).
* \(\varepsilon=1,1\le s\le q:\ r=s\) or \(n-s+1\le r\le n\).
* \(\varepsilon=1,s=n:\ 0\le r\le n\).
* \(\varepsilon=0,1\le s<q:\ n-s+1\le r\le n\).
* \(\varepsilon=0,s=q:\ r=1\) or \(3\le r\le n\).
* \(\varepsilon=0,s=n:\ 2\le r\le n\).

All endpoints are included. In particular, at zero central mass and \(s=q\), the intermediate Fourier ray count \(r=2\) is impossible even though both \(r=1\) and every \(r\ge3\) occur. The isolated diagonal branch \(r=s\) for positive central mass is another consequence of the positivity constraint.

## Assumptions and scope
Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\), and use the standard nondegenerate pairing on \(G\), with \(\widehat f(\xi)=\sum_{x\in G} f(x)\psi(-x\cdot\xi)\). For each primal ray \(L_i\), write \(b_i=f(x)\) for \(x\in L_i\setminus\{0\}\), and set \(a=f(0)\ge0\) and \(S=\sum_{i=1}^{n}b_i\). There are exactly \(s\) positive values among the \(b_i\). Orthogonality maps primal rays bijectively to dual rays; relabel the dual rays accordingly. The complete claim concerns all nonnegative *real* ray-invariant functions, not arbitrary functions or those required to have nonnegative Fourier transforms.

## Proof
The character identity \(\sum_{t\in\mathbb F_q^\times}\psi(tu)=q-1\) when \(u=0\), and \(-1\) otherwise, gives the exact ray-reduced Fourier transform
\[
\widehat f(0)=a+(q-1)S>0,\qquad
\widehat f(\xi)=a-S+q b_i\quad(0\ne\xi\in L_i^\perp).
\tag{1}
\]
Thus a nonzero dual ray is absent exactly when \(q b_i=S-a\). The formula works in all characteristics and for every nontrivial additive character.

**Positive central value.** Suppose \(a>0\). If \(a>S\), no Fourier ray vanishes, giving \(r=n\). If \(a=S\), exactly the zero primal weights correspond to zero dual rays, giving \(r=s\); here \(s\ge1\). If \(a<S\), write \(c=(S-a)/q>0\). Every primal zero weight yields a nonzero dual weight, and precisely those active \(b_i=c\) yield vanishing dual rays. Let \(m\) be the number of these active equalities, so \(r=n-m\). For \(m=s\), the equality \(a=(s-q)c>0\) forces \(s>q\), hence \(s=n\). Otherwise \(0\le m\le s-1\), giving \(n-s+1\le r\le n\). For \(s=0\), only \(r=n\) is possible. For \(s=n\), every \(m\in\{0,\ldots,n\}\) is possible, hence every \(r\).

**Zero central value.** Suppose \(a=0\); then \(s\ge1\) and \(c=S/q>0\). Again \(r=n-m\), where \(m\) is the number of active weights equal to \(c\), and \(\sum b_i=q c\). If \(s<q\), it is impossible that all active weights equal \(c\), hence \(0\le m\le s-1\). If \(s=q\), equality at all \(q\) active weights is possible, while equality at exactly \(q-1\) is impossible: the last positive weight must also equal \(c\). Every \(m\le q-2\) is possible. If \(s=n=q+1\), there must be at least two positive weights different from \(c\): equality at \(q\) weights would exhaust the sum and force the remaining positive weight to vanish. Hence \(0\le m\le q-1\). These inequalities yield exactly the remaining three cases.

**Explicit sufficiency.** Choose any \(s\) primal rays; set all other ray values to zero. The following recipes use positive rational numbers and give every listed \(r\):

* If \(a>0,s=0\), take \(a=1\). If \(1\le s\le q\) and \(r=s\), put \(b_i=1\) on all active rays and \(a=s\). For any \(s\ge1\) and \(r=n-m\) with \(0\le m\le s-1\), put \(m\) active values equal to \(1\), the other \(s-m\) active values equal to \(q+1\), and \(a=S-q>0\). If \(s=n,r=0\), take all \(b_i=1\) and \(a=1\).
* If \(a=0,1\le s<q\) and \(r=n-m\) with \(0\le m\le s-1\), take \(m\) active values equal to \(1\) and the remaining \(s-m\) equal to \((q-m)/(s-m)>1\). Then \(S=q\), and exactly \(m\) Fourier rays vanish.
* If \(a=0,s=q,r=1\), put all \(q\) active values equal to \(1\). For \(r=n-m\) with \(0\le m\le q-2\), put \(m\) values equal to \(1\); among the remaining \(k=q-m\ge2\), put \(k-1\) values equal to \(1+\delta\) and the last equal to \(1-(k-1)\delta\), where \(\delta=1/(2(k-1))\). Then \(S=q\), all values are positive, and precisely \(m\) equal \(1\).
* If \(a=0,s=n\) and \(r=n-m\) with \(0\le m\le q-1\), put \(m\) values equal to \(1\) and each of the other \(n-m\) values equal to \((q-m)/(n-m)\in(0,1)\). Then \(S=q\) and precisely \(m\) values equal \(1\).

The formulas for \(r\) follow immediately from (1). Therefore every and only every advertised triple is realized. \(\square\)

## Verification
The proof uses a finite-field character identity and exact inequalities; no enumeration or numerical approximation is needed. The accompanying standalone checker verifies the ray-reduced formula against direct finite Fourier sums for representative prime fields, and checks that enumerated nonnegative small-integer weights yield no triples outside the stated diagram. The calculations corroborate, but do not replace, the quantified proof.

## Relationship to prior work
The finite-field wavelet/bandwidth framework of Iosevich, Liu, Mayeli and Pakianathan develops support along projective directions and equidistribution through Fourier zeros [1]. Kiss, Matolcsi, Matolcsi and Somlai explicitly use ray-type functions, and their Lemma 2.4 records the Fourier transform of sums of line indicators in connection with positive-definite tilings [2]. Those ingredients explain the elementary Fourier reduction (1). The statement here is the complete *existential* attainable-support diagram for arbitrary nonnegative ray-invariant weights, separating the origin-supported and origin-vanishing cases and supplying constructions for every allowed pair. In particular it does not assert a new transform formula, a new uncertainty inequality for unrestricted functions, or a positive-definite tiling theorem.

## Limitations
This is only the two-dimensional scalar-invariant class, with nonnegative real amplitudes. No claim is made about higher-dimensional projective incidence, prescribed spatial positions beyond ray support, or functions with sign changes. The underlying ray-transform identity is known; the scientific distinction is the complete positivity-constrained realizability classification. Equivalent unlocated support classifications remain possible.

## References
[1] A. Iosevich, A. Liu, A. Mayeli, J. Pakianathan, *Wavelet decomposition and bandwidth of functions defined on vector spaces over finite fields*, arXiv:1601.03473v1, first submitted 2016-01-14, especially Sections 2–4. https://arxiv.org/html/1601.03473v1

[2] G. Kiss, D. Matolcsi, M. Matolcsi, G. Somlai, *Tiling and weak tiling in \((\mathbb Z_p)^d\)*, published online 2023-12-04, especially Definition 2.2, Lemma 2.4, and Proposition 3.1. https://doi.org/10.1007/s43670-023-00073-7
