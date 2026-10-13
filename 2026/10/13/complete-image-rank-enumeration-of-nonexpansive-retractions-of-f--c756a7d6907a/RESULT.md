# Complete image-rank enumeration of nonexpansive retractions of finite chains

## Finding
For every integer \(n\ge1\), let \(\mathcal{CT}_n\) be the monoid of all full contractions \(f:[n]\to[n]\), meaning \(|f(i)-f(j)|\le |i-j|\) for all \(i,j\). Write \(c_{n,r}\) for the number of composition-idempotents \(f^2=f\) with \(|\operatorname{im}f|=r\). For every \(1\le r\le n\), set \(M_r=(m_{ij})_{1\le i,j\le r}\), where \(m_{ij}=1\) if \(|i-j|\le1\) and otherwise \(m_{ij}=0\); denote the all-one column by \(\boldsymbol1\) and the first standard basis column by \(e_1\). Then
\[
\boxed{c_{n,r}=[z^{n-r}]\left(\boldsymbol1^{\mathsf T}(I-zM_r)^{-1}e_1\right)^2.}
\]
Equivalently, if \(u_r(t)=\boldsymbol1^{\mathsf T}M_r^t e_1\), then
\[
\boxed{c_{n,r}=\sum_{a=0}^{n-r}u_r(a)u_r(n-r-a).}
\]
This supplies every image-rank coefficient of the idempotent-count polynomial \(\sum_{r=1}^n c_{n,r}T^r\), including all interior ranks. In particular, the rank-three generating function is
\[
\sum_{n\ge3}c_{n,3}z^{n-3}=\frac1{(1-2z-z^2)^2}.
\]
For \(n=7\), the full polynomial is
\[
7T+192T^2+131T^3+46T^4+14T^5+4T^6+T^7,
\]
so the monoid has \(395\) idempotents. The coefficient \(c_{7,3}=131\) contradicts the prediction \(130\) of Conjecture 14 in Zubairu and Ali, *On the Idempotents of Semigroup of Partial Contractions of a Finite Chain* (2021), as verified against its displayed formula.

## Assumptions and scope
The domain \([n]=\{1,\ldots,n\}\) has its ordinary integer metric. A full contraction is not assumed order-preserving: its successive values may rise, remain level, or fall. An idempotent means \(f\circ f=f\) and is necessarily a retraction onto its fixed-point set. No partial maps are counted. The bounds \(n\ge1\) and \(1\le r\le n\) include the singleton and identity cases; set \(c_{n,r}=0\) outside this rank range.

## Proof
**1. Consecutive fixed image.** The Lipschitz condition is equivalent to \(|f(i+1)-f(i)|\le1\) for \(1\le i<n\): the general condition follows by summing adjacent inequalities. Thus the sequence \((f(1),\ldots,f(n))\) visits every integer between its minimum and maximum, so its image is an integer interval. If \(f^2=f\), each image point is fixed. Therefore there is a unique integer \(a\), \(1\le a\le n-r+1\), for which the image is \(I_a=\{a,a+1,\ldots,a+r-1\}\), with \(f(i)=i\) for all \(i\in I_a\).

**2. Independent exterior walks.** Once \(I_a\) is fixed, the values \(f(a-1), f(a-2),\ldots,f(1)\) form a length-\(a-1\) walk inside \(I_a\), started at the fixed value \(f(a)=a\), with allowed steps \(0,1,-1\). The right tail \(f(a+r),\ldots,f(n)\) similarly starts from the opposite boundary \(f(a+r-1)=a+r-1\). All adjacent inequalities across the three pieces hold exactly when both walks are allowed, and the triangle inequality then gives global contraction. Conversely, the fixed interval and any pair of such walks define an idempotent because every image lies in the fixed interval. The two choices are independent. By reflecting the interval, both boundary-started walk counts equal \(u_r(t)=\boldsymbol1^{\mathsf T}M_r^t e_1\). The left and right lengths are \(a-1\) and \(n-(a+r-1)\). Summing over all \(a\) proves the convolution formula, and multiplying ordinary generating series proves the coefficient formula.

**3. The rank-three case and published conjecture.** Direct inversion for \(r=3\) gives \(\boldsymbol1^{\mathsf T}(I-zM_3)^{-1}e_1=1/(1-2z-z^2)\). Hence \(u_3(0),\ldots,u_3(4)=(1,2,5,12,29)\), and the five possible locations of a three-point image inside \([7]\) contribute, respectively, \(29,24,25,24,29\). Their sum is \(131\). The coefficients of the published Conjecture 14 satisfy \(a_6=12\) and \(a_7=29\); its stated formula \(2(a_n+(n-4)a_{n-1})\) consequently gives \(2(29+3\cdot12)=130\) at \(n=7\). The discrepancy is one and is independently confirmed by exhaustive enumeration; the conjecture as stated cannot hold universally.

**4. Boundary ranks.** For \(r=1\), the only boundary walk is constant, so \(c_{n,1}=n\). For \(r=2\), every step may choose either endpoint, so \(u_2(t)=2^t\) and \(c_{n,2}=(n-1)2^{n-2}\) for \(n\ge2\). Also \(c_{n,n}=1\); for \(n\ge3\), \(c_{n,n-1}=4\), and for \(n\ge5\), \(c_{n,n-2}=14\). These agree with the published established boundary-rank results, and are not claimed as new.

## Verification
The bundled standalone `checker.py` requires only Python's standard library. Run `python3 checker.py`. It independently enumerates all functions \([n]\to[n]\) for \(1\le n\le7\), selects those with adjacent jumps of size at most one and \(f^2=f\), and compares their entire image-rank counts to the transfer-matrix formula. It also verifies the five image-interval contributions for \((n,r)=(7,3)\), checks the closed forms for boundary ranks and compares the published conjecture's value at \(n=7\). A successful execution prints `VERIFY_OK`. The exhaustive check is finite; the all-\(n\) theorem follows from the preceding bijection, not from this test.

## Relationship to prior work
Umar and Zubairu (arXiv:1804.10057v1, public on 2018-04-25), give the structural theory of full contraction semigroups, including their regularity and Green relations, but not this all-ranks enumeration. Zubairu and Ali (2021, DOI 10.47495/okufbed.799385) prove the rank-one, rank-two and near-full-rank counts, explicitly identify intermediate ranks as open in their final section, and state Conjecture 14 for image rank three. The present coefficient formula covers every rank and, at \(n=7\), gives a counterexample to that conjecture. Ojo, Al-Kharousi and Umar (2021, DOI 10.4236/ojdm.2021.113007) treat order-preserving *partial* contractions, a different mapping class; their enumeration does not imply the unrestricted full-contraction rank distribution. The findings do not assert priority over inaccessible or uncatalogued work under alternate terminology.

## Limitations
This result is for full nonexpansive self-maps of finite paths, not arbitrary finite graphs, weighted metrics, or partial contractions. It counts maps by image cardinality, not Green-class isomorphism type or ordered pairs of idempotents. The published-conjecture comparison is to the exact displayed formula in the cited 2021 paper, not to a possible subsequently amended conjecture. No independent scientific audit has been performed.

## References
1. A. Umar and M. M. Zubairu, *On certain semigroups of full contractions of a finite chain*, arXiv:1804.10057v1 (first posted 2018-04-25), https://arxiv.org/abs/1804.10057.
2. M. M. Zubairu and B. Ali, *On the Idempotents of Semigroup of Partial Contractions of a Finite Chain*, Osmaniye Korkut Ata University Journal of The Institute of Science and Technology 4 (2021), 233–241, DOI 10.47495/okufbed.799385; open PDF https://dergipark.org.tr/en/download/article-file/1307229.
3. O. A. Ojo, F. S. A. Al-Kharousi and A. Umar, *On the Number of Idempotent Partial Contraction Mappings of a Finite Chain*, Open Journal of Discrete Mathematics 11 (2021), 94–101, DOI 10.4236/ojdm.2021.113007.
