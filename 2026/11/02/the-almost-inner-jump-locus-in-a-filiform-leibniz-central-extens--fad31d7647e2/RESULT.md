# The almost-inner jump locus in a filiform Leibniz central-extension family

## Finding
For every field \(K\), every integer \(n\ge4\), and all \(\theta_1,\theta_2,\theta_3\in K\), define the \(n\)-dimensional right Leibniz algebra \(L_n(\theta_1,\theta_2,\theta_3)\) by the multiplication in the next section. Let \(\operatorname{AID}(L)\) be the linear space of derivations \(D\) such that \(D(x)\in[x,L]\) for every \(x\), and let \(\operatorname{Inn}(L)=\{R_y:y\in L\}\), with \(R_y(x)=[x,y]\). Let \(E\) send \(e_2\) to \(e_n\) and vanish on all other basis elements. Then
\[
\operatorname{AID}(L_n)=\begin{cases}
\operatorname{Inn}(L_n),&\theta_3=0,\\
\operatorname{Inn}(L_n)\oplus K E,&\theta_3\ne0.
\end{cases}
\]
The inner-derivation space has dimension \(n-1\). Consequently, for \(K=\mathbb F_q\), the numbers of almost-inner derivations are exactly \(q^{n-1}\) and \(q^n\), respectively. Thus the jump locus in this three-parameter family is precisely the complement of the hyperplane \(\theta_3=0\), in every characteristic.

This corrects the parameter-independent assertion in Proposition 3.14 of Adashev and Kurbanbaev (2020), which states a nonzero \(K E\) summand for every parameter choice: when \(\theta_3=0\), already \(E(e_2)=e_n\notin[e_2,L_n]=K e_3\).

## Assumptions and scope
Write \(L_n=\bigoplus_{i=1}^{n}K e_i\). Its potentially nonzero brackets are
\[
[e_1,e_1]=\theta_1e_n,\quad [e_1,e_2]=-e_3+\theta_2 e_n,\quad [e_2,e_2]=\theta_3 e_n,
\]
\[
[e_i,e_1]=e_{i+1}\ (2\le i\le n-1),\qquad
[e_1,e_i]=-e_{i+1}\ (3\le i\le n-1).
\]
All omitted brackets are zero. The structure is a central modification of the standard \(n\)-dimensional naturally graded filiform Lie multiplication; equivalently, it is a one-dimensional central extension of the corresponding \((n-1)\)-dimensional quotient. The modified terms are central and involve only generator pairs. It obeys the **right Leibniz** identity \([x,[y,z]]=[[x,y],z]-[[x,z],y]\), including in characteristic two. This is the subfamily with all higher \(\beta\)-parameters equal to zero, not a claim about every filiform Leibniz algebra.

## Proof
For the stated right Leibniz identity, every \(R_y\) is a derivation. Let \(D\in\operatorname{AID}(L_n)\). Since \(D(e_1)\in[e_1,L_n]\), subtract some \(R_y\) and obtain a derivation \(D'\) with \(D'(e_1)=0\). The product table gives
\[
[e_2,L_n]=K e_3+K\theta_3 e_n.
\]
As \(n\ge4\), \(e_3\) and \(e_n\) are linearly independent. Write \(D'(e_2)=a e_3+b e_n\), with \(b=0\) if \(\theta_3=0\). Applying the derivation identity successively to \([e_i,e_1]=e_{i+1}\) yields
\[
D'(e_i)=a e_{i+1}\quad(3\le i\le n-1),\qquad D'(e_n)=0.
\]
Define \(S=R_{e_1+\theta_1 e_{n-1}}\). Directly from the multiplication table, \(S(e_1)=0\), \(S(e_i)=e_{i+1}\) for \(2\le i\le n-1\), and \(S(e_n)=0\). Thus \(D'=aS+bE\) and
\[
\operatorname{AID}(L_n)\subseteq\operatorname{Inn}(L_n)+K E.
\]
The map \(E\) is a derivation: it annihilates the derived algebra \(\langle e_3,\ldots,e_n\rangle\), and its image lies in the central line \(K e_n\).

If \(\theta_3=0\), then \(E(e_2)=e_n\notin[e_2,L_n]=K e_3\), so \(E\) is not almost inner and the previous upper bound forces \(\operatorname{AID}(L_n)=\operatorname{Inn}(L_n)\).

If \(\theta_3\ne0\), take any \(x=\sum_{i=1}^{n}x_i e_i\). If \(x_1\ne0\), then \([x,e_{n-1}]=-x_1e_n\), so \(E(x)=x_2e_n=[x,-(x_2/x_1)e_{n-1}]\). If \(x_1=0\) and \(x_2\ne0\), then \([x,e_2]=x_2\theta_3e_n\), so \(E(x)=[x,\theta_3^{-1}e_2]\). If both coefficients vanish, \(E(x)=0\). Hence \(E\in\operatorname{AID}(L_n)\).

Furthermore, \(E\notin\operatorname{Inn}(L_n)\): if \(R_y(e_2)=e_n\), comparing the \(e_3\) and \(e_n\) coefficients forces the \(e_1\)-coefficient of \(y\) to vanish and the \(e_2\)-coefficient to equal \(\theta_3^{-1}\). But then \(R_y(e_1)\) has nonzero \(e_3\)-coefficient \(-\theta_3^{-1}\), contradicting \(E(e_1)=0\). The sum is direct. Finally, the right annihilator is precisely \(K e_n\): evaluating \(R_y(e_2)=0\) and then \(R_y(e_1)=0\) successively forces all coefficients of \(y\) except that of \(e_n\) to vanish. Therefore \(\dim\operatorname{Inn}(L_n)=n-1\), proving the dimension and finite-field formulas.

## Verification
The standalone `verify.py` constructs the bracket directly and checks the right Leibniz identity and derivation identities on all basis triples for 60 configurations with \(n=4,5,6,7\), primes \(2,3,5\), and five central-parameter choices each. It independently enumerates every vector in each test field to verify the pointwise condition for \(E\), and for eight selected cases it solves the derivation linear equations and exhausts **all** derivations, reproducing the predicted almost-inner dimensions without assuming the theorem. Invoke `python3 verify.py` from the extracted package directory. These finite checks support, but do not replace, the characteristic-free proof.

## Relationship to prior work
Adashev and Kurbanbaev, *Almost inner derivations of some nilpotent Leibniz algebras* (first arXiv submission October 2, 2020), introduce the exact \(F_3\) multiplication family in §3.12. Their Theorem 3.13 supplies an upper-bound normal form, while their Proposition 3.14 asserts that the extra \(E_{n,2}\) direction always occurs. The present criterion identifies its precise occurrence locus and gives an independent argument, so it is not a new claim for the already known general upper bound. Burde, Dekimpe, and Verbeke (2019) study almost-inner derivations of Lie algebras, a setting that overlaps the all-zero-parameter special case but not the full non-Lie central-extension family. Khudoyberdiyev and Omirov (2013) study deformation/cohomological structure of these filiform Leibniz models, rather than the pointwise almost-inner locus. A later study by Kurbanbaev (2023) treats thin and solvable Leibniz families, not the parameter classification asserted here.

## Limitations
The theorem treats exactly the displayed three-parameter central-extension subfamily, with higher \(\beta\)-parameters zero; no classification is asserted for the full \(F_3\) list with additional brackets. The finite-field count is an immediate consequence of the exact dimension, not a count of all derivations or of automorphisms. An earlier equivalent correction or general AID classification beyond the inspected literature remains a publication-priority risk. The result has not received independent mathematical audit.

## References
1. J. K. Adashev and T. K. Kurbanbaev, *Almost inner derivations of some nilpotent Leibniz algebras*, arXiv:2010.01904v1 (October 2, 2020), especially §§2–3 and Proposition 3.14. https://arxiv.org/html/2010.01904v2
2. D. Burde, K. Dekimpe, and B. Verbeke, *Almost inner derivations of Lie algebras II*, arXiv:1905.08145 (May 20, 2019). https://arxiv.org/abs/1905.08145
3. A. Kh. Khudoyberdiyev and B. A. Omirov, *Infinitesimal deformations of naturally graded filiform Leibniz algebras*, arXiv:1305.2676 (May 13, 2013). https://arxiv.org/abs/1305.2676
4. T. K. Kurbanbaev, *Almost Inner Derivations of Some Leibniz Algebras*, Journal of Siberian Federal University Mathematics & Physics 16 (2023), no. 4. https://elib.sfu-kras.ru/handle/2311/150181
