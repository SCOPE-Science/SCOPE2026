# A sharp octahedrality threshold for a three-parameter Lipschitz-free family

## Finding
Let
\[
M(a,b,c)=\{o,z\}\cup\{x_n:n\in\mathbb N\}
\]
carry the distances
\[
d(o,x_n)=a,\qquad d(x_n,x_m)=a\ (n\ne m),\qquad d(z,x_n)=b,\qquad d(o,z)=c.
\]
Assume
\[
a,b,c>0,\qquad a\le 2b,\qquad |a-b|\le c\le a+b.
\]
These conditions are exactly the triangle inequalities for this family. Then the Lipschitz-free space \(\mathcal F(M(a,b,c))\) has an octahedral norm if and only if
\[
c\le b.
\]
For the two-point set \(\{o,z\}\), the exact optimal long-trapezoid ratio is
\[
\Theta(a,b,c)=\max\left\{\frac{a+b}{a+c},\frac{a}{b+c}\right\}.
\]
Thus \(c>b\) gives the sharp obstruction \(\Theta(a,b,c)<1\), while \(c\le b\) admits exact long-trapezoid witnesses with no loss.

## Assumptions and scope
The statement concerns the real Lipschitz-free space over the pointed metric space above, with \(o\) as base point. The metric conditions follow by checking the only nontrivial triangle types: \((b,b,a)\) and \((a,b,c)\). The proof uses the characterization of octahedrality of \(\mathcal F(M)\) by the long trapezoid property.

## Proof
By the long trapezoid characterization, \(\mathcal F(M)\) is octahedral exactly when for every finite \(N\subset M\) and every \(\varepsilon>0\) there exist distinct \(u,v\in M\) such that
\[
(1-\varepsilon)\bigl(d(x,y)+d(u,v)\bigr)\le d(x,u)+d(y,v)
\]
for all \(x,y\in N\).

Assume first that \(c\le b\). Given finite \(N\), choose distinct fresh points \(u=x_i\) and \(v=x_j\) outside \(N\). Then \(d(u,v)=a\). We prove the stronger inequality
\[
d(x,y)+a\le d(x,u)+d(y,v)
\]
for every \(x,y\in N\). If neither point is \(z\), the right side is \(2a\) and the left side is at most \(2a\). If one point is \(z\) and the other is some \(x_k\), both sides equal \(a+b\). For \((x,y)=(z,o)\) or \((o,z)\), the left side is \(a+c\le a+b\), which equals the right side. For \(x=y=z\), the required inequality is \(a\le 2b\), already part of the metric conditions. Hence the long trapezoid property holds, even with \(\varepsilon=0\).

Conversely assume \(c>b\), and take \(N=\{o,z\}\). For any distinct \(u,v\), both orientations of the long-trapezoid inequality imply
\[
1-\varepsilon\le Q(u,v):=
\frac{\min\{d(o,u)+d(z,v),\ d(z,u)+d(o,v)\}}{c+d(u,v)}.
\]
There are only four unordered pair types. If \(u,v\) are two distinct \(x\)-points, then
\[
Q(u,v)=\frac{a+b}{a+c}.
\]
For a pair of type \(\{o,x_n\}\),
\[
Q(u,v)=\frac{b}{a+c},
\]
which is no larger than \((a+b)/(a+c)\). For a pair of type \(\{z,x_n\}\), the triangle inequality \(a\le b+c\) gives
\[
Q(u,v)=\frac{a}{b+c}.
\]
Finally, for \(\{o,z\}\), the numerator vanishes. Therefore
\[
\sup_{u\ne v}Q(u,v)=\max\left\{\frac{a+b}{a+c},\frac{a}{b+c}\right\}.
\]
When \(c>b\), the first term is strictly below \(1\). The second is also strictly below \(1\): equality \(a=b+c\) together with \(c>b\) would force \(a>2b\), contradicting the metric condition. Hence \(\Theta(a,b,c)<1\). Choosing \(\varepsilon>0\) with \(1-\varepsilon>\Theta(a,b,c)\) makes the long trapezoid property fail on \(N=\{o,z\}\). Thus \(\mathcal F(M(a,b,c))\) is not octahedral.

## Verification
The proof reduces the infinite family to finitely many pair and triangle types. The accompanying exact-rational checker enumerates those pair types over a grid of admissible rational parameters, verifies the closed formula for \(\Theta\), checks exact witnesses when \(c\le b\), and checks \(\Theta<1\) when \(c>b\). This computation is a consistency check; the theorem itself is proved symbolically above.

## Relationship to prior work
Procházka and Rueda Zoca proved that octahedrality of a Lipschitz-free space is equivalent to the long trapezoid property, and their Example 3.6 gives the special metric with \((a,b,c)=(1,1,2)\) as a non-octahedral example. The result here classifies the entire natural three-parameter homogeneous extension of that example and identifies both the exact threshold \(c=b\) and the exact two-point obstruction ratio. A later paper of Langemets and Rueda Zoca studies octahedrality of duals and biduals of Lipschitz-free spaces and related metric families, but the inspected material does not contain this three-parameter classification.

## Limitations
The classification is only for this highly symmetric countable family. It does not classify arbitrary one-point extensions of uniformly discrete metric spaces, nor does it address octahedrality of \(\operatorname{Lip}_0(M)\) or bidual phenomena. The originality check covered targeted semantic searches and the most directly relevant primary papers; differently phrased or unindexed literature may still contain an equivalent elementary classification.

## References
1. A. Procházka and A. Rueda Zoca, “A characterisation of octahedrality in Lipschitz-free spaces,” *Annales de l'Institut Fourier* 68 (2018), arXiv:1612.03808, DOI 10.5802/aif.3171.
2. J. Langemets and A. Rueda Zoca, “Octahedral norms in duals and biduals of Lipschitz-free spaces,” arXiv:1905.09061.
