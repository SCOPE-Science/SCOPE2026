# Maximum Frobenius dimension of quasi-hereditary Nakayama algebras

## Result

Let \(k\) be an algebraically closed field and let \(A\) be a connected basic finite-dimensional Nakayama \(k\)-algebra with \(n\ge 2\) simple modules. Define its Frobenius dimension by
\[
F(A)=\dim_k\operatorname{Hom}_A(D(A),A).
\]
If \(A\) is quasi-hereditary, then
\[
\boxed{F(A)\le n^2+1.}
\]
The bound is sharp for every \(n\ge2\). Consequently, the maximal Frobenius dimension among connected basic quasi-hereditary Nakayama algebras with \(n\) simple modules is exactly
\[
\boxed{n^2+1.}
\]

One extremal cyclic Nakayama algebra has Kupisch series
\[
[n,\,2n-1,\,2n-2,\ldots,n+1].
\]

This answers Question 2 in the 2020 MathOverflow question “Frobenius dimensions of Nakayama algebras” in the standard basic connected setting used for Kupisch-series classification.

## Setup for cyclic Nakayama algebras

Index the simple right modules periodically by \(S_i\), \(i\in\mathbb Z\), with \(S_{i+n}=S_i\). Let
\[
P_i=e_iA
\]
have length \(c_i\), where \(c_{i+n}=c_i\). Write
\[
r_i=i+c_i-1.
\]
The Kupisch inequalities \(c_{i+1}+1\ge c_i\) are equivalent to
\[
r_i\le r_{i+1},
\qquad
r_{i+n}=r_i+n.
\]

It is convenient to represent an indecomposable uniserial module by an integer interval: \(P_i\) has composition factors
\[
S_i,S_{i+1},\ldots,S_{r_i}.
\]
For an integer \(y\), define
\[
\ell(y)=\min\{x\in\mathbb Z:r_x\ge y\}.
\]
Then the indecomposable injective with socle \(S_y\) is represented by
\[
I_y=[\ell(y),y],
\]
of length \(y-\ell(y)+1\). This is the usual coKupisch description in interval form.

For two uniserial modules
\[
U=[a,a+d-1],\qquad V=[j,j+c-1]
\]
on the cyclic quiver, a homomorphism \(U\to V\) is determined by an allowed image of the top of \(U\). Hence
\[
\dim_k\operatorname{Hom}_A(U,V)
\]
is the number of integers \(t\) such that
\[
\max(0,c-d)\le t<c,\qquad j+t\equiv a\pmod n.
\tag{1}
\]
Equivalently, it counts the occurrences of the top simple of \(U\) in the terminal \(\min(c,d)\) composition factors of \(V\).

Since
\[
D(A)\cong\bigoplus_{i=0}^{n-1} I_i,
\qquad
A\cong\bigoplus_{j=0}^{n-1}P_j,
\]
we have
\[
F(A)=\sum_{i,j}\dim_k\operatorname{Hom}_A(I_i,P_j).
\tag{2}
\]

## Linear case

Every connected linear Nakayama algebra is quasi-hereditary. In a linear Nakayama algebra, an indecomposable projective contains each simple composition factor at most once. Formula (1) therefore gives
\[
\dim_k\operatorname{Hom}_A(I_i,P_j)\le1
\]
for every \(i,j\). Thus
\[
F(A)\le n^2<n^2+1.
\tag{3}
\]

## Cyclic case: the single possible double Hom

Suppose now that \(A\) is cyclic and quasi-hereditary. A theorem of Uematsu–Yamagata, in the Kupisch-series form recorded by Marczinzik–Rubey–Stump, says that some simple has projective dimension \(2\). Rotate the indices so that this is \(S_0\).

Marczinzik–Rubey–Stump's projective-dimension criterion is
\[
c_1+1=c_0+c_{c_0}.
\tag{4}
\]
Set \(p=c_0\). Since \(r_0=p-1\), equation (4) is exactly
\[
r_1=r_p.
\tag{5}
\]
Because \(r_i\) is nondecreasing,
\[
r_1=r_2=\cdots=r_p=:R.
\tag{6}
\]
Periodicity rules out \(p>n\): otherwise the plateau in (6) would contain indices differing by \(n\), contradicting \(r_{i+n}=r_i+n\). Hence
\[
p\le n.
\tag{7}
\]

For \(1\le x\le n\),
\[
r_x\le r_n=r_0+n=p+n-1.
\tag{8}
\]
It follows that every indecomposable projective has length at most \(2n-1\). The same bound holds for injectives: if \(x=\ell(y)\) is chosen with \(1\le x\le n\), then
\[
r_{x-1}<y\le r_x\le p+n-1,
\]
so
\[
\ell(I_y)=y-x+1\le p+n-x\le2n-1.
\tag{9}
\]
By (1), every \(\operatorname{Hom}(I_i,P_j)\) therefore has dimension at most \(2\).

We now show that dimension \(2\) can occur for at most one pair.

Assume \(I_y=[x,y]\), with \(1\le x\le n\), has length \(>n\). Then
\[
y\ge x+n.
\]
Since \(x=\ell(y)\),
\[
r_{x-1}<y\le r_x,
\]
so \(r_x>r_{x-1}\) and \(r_x\ge x+n\).

If \(2\le x\le p\), this contradicts the plateau (6). If \(p<x\le n\), then (8) gives
\[
r_x\le p+n-1<x+n,
\]
again a contradiction. Therefore every injective of length \(>n\) has top \(S_1\):
\[
x=1.
\tag{10}
\]

If \(\dim\operatorname{Hom}(I_y,P_j)=2\), then both the source and target have length \(>n\), and \(P_j\) must contain two occurrences of the top simple \(S_1\) in the eligible terminal segment. Represent the projectives by starts \(j=1,\ldots,n\). The endpoint bound \(r_j\le r_n\le2n-1\) shows that a projective starting at \(j\ge2\) cannot contain two integers congruent to \(1\pmod n\); and \(P_n\) has length \(c_0=p\le n\). Hence necessarily
\[
j=1.
\tag{11}
\]

Now \(P_1=[1,R]\). An injective with top \(S_1\) is \([1,y]\) with \(y\le R\). For the occurrence of \(S_1\) at the very top of \(P_1\) to define a homomorphism, formula (1) requires the source length to be at least \(R\), so \(y\ge R\). Therefore \(y=R\), and
\[
I_R=P_1.
\tag{12}
\]
Thus there is at most one pair \((I_i,P_j)\) for which the Hom-space has dimension \(2\). Every other one of the \(n^2\) Hom-spaces has dimension at most \(1\). From (2),
\[
F(A)\le (n^2-1)\cdot1+2=n^2+1.
\tag{13}
\]

## Sharpness

For every \(n\ge2\), take the cyclic Nakayama algebra with Kupisch series
\[
[c_0,c_1,\ldots,c_{n-1}]
=
[n,\,2n-1,\,2n-2,\ldots,n+1].
\tag{14}
\]
Its endpoint sequence satisfies
\[
r_0=n-1,\qquad r_1=r_2=\cdots=r_n=2n-1.
\]
In particular,
\[
c_1+1=2n=c_0+c_{c_0},
\]
so \(S_0\) has projective dimension \(2\); hence the algebra is quasi-hereditary.

The \(n\) injectives may be lifted to the intervals
\[
I_i=[1,n+i],\qquad 0\le i\le n-1.
\]
Every pair \((I_i,P_j)\) admits a nonzero homomorphism. Indeed, \(P_0=[0,n-1]\) contains the occurrence \(1\) of the source top and each \(P_j=[j,2n-1]\), \(1\le j\le n-1\), contains the occurrence \(n+1\), with the corresponding terminal segment no longer than the appropriate shifted injective. In addition,
\[
I_{n-1}=P_1=[1,2n-1],
\]
and its endomorphism space has dimension \(2\), with the two maps corresponding to the two occurrences \(1\) and \(n+1\) of its top simple. By the uniqueness argument above, this is the only double Hom. Hence
\[
F(A)=n^2+1.
\]

Combining this with (3) and (13) proves the theorem.

## Context and limitations

The 2020 MathOverflow question explicitly reports the initial maxima
\[
5,10,17,26,37,50,65
\]
and conjectures \(n^2+1\). The proof above explains the simple formula: quasi-heredity forces a plateau in the cyclic Nakayama endpoint function, which in turn allows at most one Hom-space between an indecomposable injective and an indecomposable projective to have multiplicity \(2\); all other \(n^2-1\) pairs contribute at most one dimension.

The statement is made for connected basic Nakayama algebras over an algebraically closed field, matching the standard Kupisch-series/quiver setting of the cited classification literature. It does not address Question 1 from the same MathOverflow post, concerning whether \(F(A)\ge\operatorname{gldim}(A)\) for arbitrary finite-global-dimension Nakayama algebras.

Originality is asserted only to the best of our knowledge. The MathOverflow page still has no posted answer, and targeted searches for the exact extremal formula and synonymous formulations did not locate a later solution. Recent work on quasi-hereditary Nakayama algebras concerns their homological classifications and orderings rather than this invariant. A 2026 preprint, *Bounds on Frobenius dimension* (arXiv:2607.15999), is directly relevant to the invariant and its abstract gives general dimension bounds plus formulas for truncated path algebras; its full text was not inspected here, so an unindexed or unstated-in-the-abstract overlap remains the principal literature risk.

## References

1. “Frobenius dimensions of Nakayama algebras,” MathOverflow, asked 28 January 2020.  
   https://mathoverflow.net/questions/351323/frobenius-dimensions-of-nakayama-algebras

2. R. Marczinzik, M. Rubey, C. Stump, “A combinatorial classification of 2-regular simple modules for Nakayama algebras,” *J. Pure Appl. Algebra* 225 (2021), 106520.  
   https://doi.org/10.1016/j.jpaa.2020.106520  
   https://arxiv.org/abs/1811.05846

3. M. Uematsu, K. Yamagata, “On serial quasi-hereditary rings,” *Hokkaido Math. J.* 19 (1990), 165–174.  
   https://www.math.sci.hokudai.ac.jp/hmj/page/19-1/HMJ_19_1_1990_165-174.html

4. R. Marczinzik, E. Sen, “A new characterization of quasi-hereditary Nakayama algebras and applications,” *Comm. Algebra* 50 (2022), 4481–4493.  
   https://doi.org/10.1080/00927872.2022.2063301

5. D. Artenstein, J. Cóppola, J. Finot, A. González, G. Mata, “Bounds on Frobenius dimension,” arXiv:2607.15999 (2026).  
   https://arxiv.org/abs/2607.15999
