# Exact uniform mean overshoot for two-point lattice renewals

## Finding

Let \(m\ge2\) be an integer and let \(0<p<1\). Put \(q=1-p\), and let
\(X_1,X_2,\ldots\) be independent and identically distributed with
\[
\Pr(X_i=m)=p,\qquad \Pr(X_i=1)=q.
\]
For
\[
S_n=\sum_{i=1}^n X_i,\qquad
\tau(t)=\inf\{n\ge1:S_n>t\},\qquad
R_t=S_{\tau(t)}-t,
\]
write
\[
\mu=\mathbb E X_i=q+pm,\qquad
\theta=\frac{\log\mu}{-\log q},\qquad
k=\lfloor\theta\rfloor.
\]
Then \(0\le k\le m-2\), and the exact uniform mean-overshoot constant is
\[
\boxed{
\sup_{t\ge0}\mathbb E R_t
=
m-k+\frac{q}{p}
-q^{k+1}\left(m+\frac{q}{p}\right).
}
\]
The supremum is attained at \(t=k\). If \(\theta\notin\mathbb Z\), this
maximizer is unique. If \(\theta\in\mathbb Z\), the complete set of
maximizers is \(t=k-1\) and \(t=k\).

There is also a natural rare-long-jump limit. For fixed \(\lambda>0\) and
\(p=\lambda/m\),
\[
\frac{1}{m}\sup_{t\ge0}\mathbb E R_t
\longrightarrow
1-\frac{\log(1+\lambda)}{\lambda}.
\]
By comparison, the classical Lorden moment bound satisfies
\[
\frac{1}{m}\frac{\mathbb E X_i^2}{\mathbb E X_i}
\longrightarrow
\frac{\lambda}{1+\lambda},
\]
and the first limit is strictly smaller for every \(\lambda>0\).

## Assumptions and scope

The result concerns ordinary renewal sums with mutually independent, identically
distributed, positive integer increments supported on the two points
\(\{1,m\}\). The boundary \(t\) is allowed to be any nonnegative real number.
The endpoints \(p=0\) and \(p=1\) are deterministic limiting cases: their
uniform mean overshoots are respectively \(1\) and \(m\).

The claim is an exact family-specific refinement of a uniform overshoot
question. It does not replace general moment bounds for arbitrary increment
laws.

## Proof

Because every \(S_n\) is integer-valued, if \(t=b+u\) with
\(b=\lfloor t\rfloor\) and \(0\le u<1\), then
\[
S_n>t\quad\Longleftrightarrow\quad S_n>b.
\]
Thus the crossing index is the same for \(t\) and \(b\), and
\[
R_t=R_b-u.
\]
Consequently \(\mathbb E R_t\) decreases linearly on every interval
\([b,b+1)\), so a global maximum must occur at an integer boundary.

Write
\[
e_b=\mathbb E R_b,\qquad b=0,1,2,\ldots.
\]
First consider \(0\le b<m\). A long jump may occur after exactly \(j\) unit
jumps, for \(0\le j\le b\), with probability \(p q^j\). Its overshoot is
\(m+j-b\). If no long jump occurs among the first \(b+1\) increments, then
\(b+1\) unit jumps cross the boundary with overshoot \(1\). Hence
\[
e_b
=
\sum_{j=0}^{b}p q^j(m+j-b)+q^{b+1}.
\]
Summing the geometric and arithmetico-geometric series gives
\[
e_b
=
m-b+\frac{q}{p}
-q^{b+1}\left(m+\frac{q}{p}\right).
\tag{1}
\]
For \(1\le b<m\), subtraction of consecutive values yields the particularly
simple increment
\[
e_b-e_{b-1}
=
\mu q^b-1.
\tag{2}
\]
Since \(q^b\) is strictly decreasing, the sequence in the initial window is
unimodal. Moreover,
\[
\mu q^b\ge1
\quad\Longleftrightarrow\quad
b\le\theta.
\]
Therefore, if \(\theta\notin\mathbb Z\), the unique maximum among
\(e_0,\ldots,e_{m-1}\) is \(e_k\). If \(\theta=k\in\mathbb Z\), then
\(e_{k-1}=e_k\), with strict increase before those two values and strict
decrease afterward.

It remains to show that \(k\) lies before the recurrence region. Define
\[
f(p)=\mu q^{m-1}
=
\bigl(1+(m-1)p\bigr)(1-p)^{m-1}.
\]
For \(0<p<1\),
\[
\frac{d}{dp}\log f(p)
=
\frac{m-1}{1+(m-1)p}
-\frac{m-1}{1-p}
<0.
\]
Since \(f(0)=1\), one has \(f(p)<1\), so
\(\theta<m-1\) and therefore \(k\le m-2\).

For every \(b\ge m\), conditioning on the first increment gives the renewal
recursion
\[
e_b=q\,e_{b-1}+p\,e_{b-m}.
\tag{3}
\]
Equation (3) is a convex combination of earlier values. Induction therefore
shows that no value after the initial window can exceed
\(\max_{0\le j<m}e_j\). Equality cannot create a new maximizer, because it
would require both predecessor values in (3) already to be maximal; the
initial maximizing set contains either one adjacent index or two adjacent
indices, and \(m\ge2\) prevents the two predecessor locations from both lying
in that set. Combining this observation with the linear decrease between
integer boundaries proves the stated global maximizer classification.
Substitution of \(b=k\) into (1) proves the exact constant.

For the scaling \(p=\lambda/m\),
\[
\frac{k}{m}\longrightarrow
\frac{\log(1+\lambda)}{\lambda},
\]
because
\[
\mu=1+\lambda-\frac{\lambda}{m},
\qquad
-m\log\left(1-\frac{\lambda}{m}\right)\longrightarrow\lambda.
\]
Also
\[
q^{k+1}\longrightarrow\frac{1}{1+\lambda}.
\]
Dividing (1) by \(m\) makes the remaining \(1/\lambda\) terms cancel, giving
\[
\frac{e_k}{m}
\longrightarrow
1-\frac{\log(1+\lambda)}{\lambda}.
\]
Finally,
\[
\frac{1}{m}\frac{\mathbb E X_i^2}{\mathbb E X_i}
\longrightarrow\frac{\lambda}{1+\lambda}.
\]
The strict comparison follows from
\[
(1+\lambda)\log(1+\lambda)>\lambda,
\]
whose left side minus \(\lambda\) is \(0\) at \(\lambda=0\) and has derivative
\(\log(1+\lambda)>0\).

## Verification

A standalone exact-rational checker accompanies this result. It independently
constructs the overshoot sequence from first-step recursions, checks the
closed form in the initial window, checks the consecutive-difference identity,
locates the exact maximizing boundary using rational inequalities rather than
floating-point logarithms, and verifies the global bound over a long finite
recurrence window for thousands of rational parameter pairs.

The computation is supplementary. The proof of the infinite-boundary claim is
the convex-combination induction in (3), not the finite enumeration.

## Relationship to prior work

Lorden introduced the classical uniform mean-overshoot problem and proved the
general moment bound
\[
\mathbb E R_t\le\frac{\mathbb E X_i^2}{\mathbb E X_i}.
\]
Carlsson and Nerman later gave an alternative renewal-inequality proof. Chang
developed further overshoot inequalities, and later inventory work derived
moment-based refinements for related undershoot quantities.

The present claim is different in form: it computes the exact uniform constant
and the complete maximizing-boundary set for the canonical two-point lattice
family \(\{1,m\}\), rather than supplying a distribution-free upper bound.
Targeted searches for two-point renewal overshoots, exact Lorden constants, and
finite-boundary residual-life extrema did not locate this formula or its
threshold \(k=\lfloor\log(\mu)/[-\log(q)]\rfloor\).

A recent public result showing failure of Lorden's classical constant under
pairwise independence was also inspected. Its construction deliberately uses
higher-order dependence; it neither implies nor contains the mutually
independent two-point calculation here. A separate public result on stationary
age/residual-life correlations concerns a different stationary functional and
does not imply this finite-boundary overshoot envelope.

## Limitations

The proof exploits both the lattice support and the special support point \(1\).
It does not give an exact uniform constant for a general two-point support
\(\{a,b\}\) when the lattice spacing and lower support point do not reduce to
this form, nor for three or more support points.

The originality assessment is based on targeted database searches and
inspection of the closest general renewal inequalities and public related
results. Older lattice-renewal literature could contain an equivalent formula
under different terminology. The full text of Lorden's 1970 article was not
available in the inspected repository view, although its abstract and
bibliographic record were checked and the classical inequality was
independently verified from the full Carlsson--Nerman proof.

## References

1. H. Carlsson and O. Nerman, “An Alternative Proof of Lorden's Renewal
   Inequality,” *Advances in Applied Probability* 18 (1986), 1015–1016.
   DOI: 10.2307/1427260. Public online release recorded 2016-07-01.
2. G. Lorden, “On Excess over the Boundary,” *The Annals of Mathematical
   Statistics* 41 (1970), 520–527. DOI: 10.1214/aoms/1177697092.
3. J. T. Chang, “Inequalities for the Overshoot,” *The Annals of Applied
   Probability* 4 (1994), 1223–1233. DOI: 10.1214/aoap/1177004913.
4. C.-H. Chiu, N.-H. Z. Leung, and K. Natarajan, “New analytical bounds on
   the average undershoot in an infinite horizon \((s,S)\) inventory system,”
   *Operations Research Letters* 41 (2013), 67–73.
   DOI: 10.1016/j.orl.2012.11.011.
