# The sharp parabolic radius of opposite quarter-turn spirallike maps

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Let \(\mathcal A\) be the normalized holomorphic functions \(f(0)=0\), \(f'(0)=1\), with \(f(z)/z\ne0\) for \(z\ne0\). For real \(\alpha\), let \(SP_\alpha\) consist of functions satisfying \(\operatorname{Re}(e^{i\alpha}zf'(z)/f(z))>0\) on \(\mathbb D\). Put \(\mathcal B=SP_{\pi/4}\cap SP_{-\pi/4}\). Let \(\mathcal P=\{w:\operatorname{Re}w>|w-1|\}\). Then the exact largest radius for which \(zf'(z)/f(z)\in\mathcal P\) for every \(f\in\mathcal B\) and all \(|z|<r\) is
\[
\boxed{R_{\mathcal P}(\mathcal B)=\frac35.}
\]
Equivalently, the sharp parabolic-starlikeness radius of the full strongly starlike class of order \(1/2\) is \(3/5\). At radius \(3/5\), the unique contact of the variability region with the parabolic boundary occurs at the real value \(1/2\).

## Assumptions and scope
All functions are holomorphic on \(\mathbb D\), normalized as stated, and satisfy the two strict spirallikeness inequalities on the entire unit disk. The parabolic region has equation \(\mathcal P=\{u+iv:v^2<2u-1\}\). Radius means an exact universal supremum; boundary points \(|z|=R\) need not lie in the open disk on which the property is asserted. No global inclusion \(\mathcal B\subset\mathcal S_{\mathcal P}\) is asserted.

## Proof
Set \(q(z)=zf'(z)/f(z)\), with the removable value \(q(0)=1\). Since \(\operatorname{Re}(e^{i\pi/4}q)>0\) and \(\operatorname{Re}(e^{-i\pi/4}q)>0\), their intersection is precisely \(|\arg q|<\pi/4\). Consequently \(p=q^2\) has positive real part and \(p(0)=1\). Conversely, every normalized holomorphic \(p\) of positive real part gives a valid member through the principal square root \(q=\sqrt p\) and \(f(z)=z\exp(\int_0^z(q(\zeta)-1)/\zeta\,d\zeta)\). Hence the variability set of \(q(z)\), over all members and \(|z|<r\), is the principal square-root image of the Carathéodory variability disk for \(p\).

By the Schwarz lemma applied to \((p-1)/(p+1)\), for \(|z|\le r<1\),
\[
\left|p(z)-\frac{1+r^2}{1-r^2}\right|\le\frac{2r}{1-r^2}.
\]
At \(r=3/5\), this is \(|p-17/8|\le15/8\), equivalent to \(4|p|^2-17\operatorname{Re}p+4\le0\). In terms of \(q=u+iv\) with \(p=q^2\), the disk condition is
\[
C(u,v):=4(u^2+v^2)^2-17(u^2-v^2)+4\le0.
\]
On the parabolic boundary \(u=(1+v^2)/2\), a direct exact expansion gives
\[
C\left(\frac{1+v^2}{2},v\right)=\frac{v^2}{4}\bigl(v^6+12v^4+21v^2+46\bigr)\ge0,
\]
with equality only at \(q=1/2\) (for which \(p=1/4\), the left boundary point of the Carathéodory disk). Thus the *open* square-root image of the Carathéodory disk does not intersect \(\partial\mathcal P\). It is connected, contains \(q=1\in\mathcal P\), and hence lies wholly in \(\mathcal P\). Therefore every admissible \(q(z)\) lies in \(\mathcal P\) whenever \(|z|<3/5\).

For sharpness take
\[
p_0(z)=\frac{1+z}{1-z},\qquad q_0(z)=\sqrt{\frac{1+z}{1-z}},\qquad f_0(z)=z\exp\left(\int_0^z\frac{q_0(\zeta)-1}{\zeta}\,d\zeta\right).
\]
This normalized function belongs to both spirallike classes since \(|\arg q_0|<\pi/4\). At \(z=-3/5\), \(q_0(z)=1/2\) touches \(\partial\mathcal P\); for every real \(z<-3/5\), \(q_0(z)<1/2\), so the parabolic condition fails. No larger radius works. The strict positivity of the displayed polynomial for \(v\ne0\) also proves uniqueness of the contact value in the variability region.

## Verification
The exact certificate is the identity for \(C((1+v^2)/2,v)\), together with \((1+(3/5)^2)/(1-(3/5)^2)=17/8\) and \(2(3/5)/(1-(3/5)^2)=15/8\). A standalone standard-library checker (`checker.py`) checks the rational coefficient identity by exact polynomial arithmetic, the endpoint radii, and both sharpness values. It supplements, not replaces, the connectedness argument and the analytic realization of \(q_0\).

## Relationship to prior work
Arul and Ravichandran (2026), Theorem 2.3, determine the parabolic-starlikeness radius separately for each single \(SP_\alpha\), by a sharp resultant equation; this does not determine the joint class \(SP_{\pi/4}\cap SP_{-\pi/4}\). Their classical \(SP_0\) radius is \(1/3\). The joint class is the full strongly starlike class of order \(1/2\), not either individual spirallike class. Lecko, Madhumitha and Ravichandran (2026) discuss the implication from parabolic starlikeness *to* strong starlikeness of order \(1/2\), but not the sharp reverse radius for the full sector class. Ali, Jain and Ravichandran (2012) treat different ratio-defined classes; and the vertical-strip class considered in arXiv:2003.04456 is not the full sector class. The new statement is a sharp reverse inclusion for normalized sector maps, with an exact algebraic tangency certificate. This comparison does not preclude a historically unindexed equivalent radius computation.

## Limitations
The result is confined to opposite spirallikeness angles \(\pm\pi/4\), equivalently strong starlikeness order \(1/2\), and to the ordinary parabolic target. It neither supplies the all-angle intersection radius nor settles the sharp radius for generalized parabolas. The conclusion uses the full joint restriction: applying either single-class radius would yield a weaker bound. Scientific priority is subject to earlier unindexed work on sharp strong-starlikeness radius inclusions.

## References
1. L. Arul and V. Ravichandran, *Radii of Starlikeness of Spirallike Functions*, arXiv:2610.06175v1 (first posted 2026-10-05), especially Theorem 2.3 and the \(\alpha=0\) case.
2. A. Lecko, S. Madhumitha and V. Ravichandran, *Radius of generalized parabolic starlikeness*, Boletín de la Sociedad Matemática Mexicana (online 2026-10-05), DOI:10.1007/s40590-026-00962-6.
3. R. M. Ali, N. K. Jain and V. Ravichandran, *On the Radius Constants for Classes of Analytic Functions*, arXiv:1207.4529v1 (2012).
4. *On a subclass of starlike functions associated with a vertical strip domain*, arXiv:2003.04456v1 (2020).
