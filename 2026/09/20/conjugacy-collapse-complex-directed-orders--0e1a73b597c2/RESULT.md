# Conjugacy collapse of explicit directed orders on the complex field

Let \(B\) be a transcendence basis of \(\mathbb R/\mathbb Q\) containing \(\pi\), and put
\[
k=\mathbb Q(B\setminus\{\pi\}).
\]
Following Wang--Yuan--Zhang--Zhu, let
\[
H_k=\{b\in\mathbb R:b\text{ is algebraic over }k\},\qquad X_k=\mathbb R\setminus H_k.
\]
For \(T\in X_k\), set
\[
t_T=T^{-1},\qquad
\mathcal O_T=\operatorname{IntCl}_{\mathbb C}\bigl(k[t_T]_{(t_T)}\bigr),
\]
and
\[
P_T=\{0\}\cup\bigcup_{n\in\mathbb Z}t_T^{-n}
\bigl(\mathbb A_{>0}+t_T\mathcal O_T\bigr),
\]
where \(\mathbb A=\overline{\mathbb Q}\cap\mathbb R\) is the field of real algebraic numbers. Their Theorem 1.2 proves the equality criterion
\[
P_T=P_U\quad\Longleftrightarrow\quad U=aT+b
\quad(a\in\mathbb A_{>0},\ b\in H_k).
\]

Let
\[
K=k\,\overline{\mathbb Q}\subseteq\mathbb C
\]
be the compositum with the algebraic closure of \(\mathbb Q\) inside \(\mathbb C\).

## Theorem

The family \(\mathcal C_k=\{P_T:T\in X_k\}\) has the following properties.

1. **A single automorphism orbit.** For every \(T,U\in X_k\), there exists
   \[
   \sigma\in\operatorname{Aut}(\mathbb C/K)
   \]
   such that
   \[
   \sigma(T)=U,\qquad \sigma(P_T)=P_U.
   \]
   Hence all ordered fields \((\mathbb C,P_T)\) in this family are isomorphic.

2. **Continuum many distinct cones.** The set \(\mathcal C_k\) has cardinality \(2^{\aleph_0}\). Thus continuum many distinct embedded orders collapse to one abstract ordered-field isomorphism class.

3. **Every nontrivial conjugacy is topologically wild.** If \(P_T\ne P_U\) and \(\tau\in\operatorname{Aut}(\mathbb C)\) satisfies \(\tau(P_T)=P_U\), then \(\tau\) is discontinuous for the usual topology on \(\mathbb C\). Equivalently, no continuous field automorphism conjugates two distinct cones in \(\mathcal C_k\).

## Proof

### 1. Transitivity under \(\operatorname{Aut}(\mathbb C/K)\)

The extension \(K/k\) is algebraic. Consequently every \(T\in X_k\) is transcendental over \(K\): if \(T\) were algebraic over \(K\), transitivity of algebraicity would make \(T\) algebraic over \(k\), contrary to \(T\in X_k\).

The source construction also uses
\[
\operatorname{trdeg}_k\mathbb R=1
\]
and proves that \(\mathbb C\) is algebraic over \(k(T)\) for every \(T\in X_k\). Hence \(\mathbb C\) is algebraic over the larger field \(K(T)\). Since \(\mathbb C\) is algebraically closed, it is an algebraic closure of \(K(T)\); similarly it is an algebraic closure of \(K(U)\).

Because \(T\) and \(U\) are transcendental over \(K\), the assignment
\[
T\longmapsto U
\]
extends uniquely to a \(K\)-isomorphism
\[
\varphi:K(T)\xrightarrow{\sim}K(U).
\]
By the standard isomorphism-extension theorem for algebraic closures, \(\varphi\) extends to a field automorphism
\[
\sigma:\mathbb C\xrightarrow{\sim}\mathbb C.
\]
It fixes \(K\), so in particular it fixes \(k\) and every algebraic number.

Now \(\sigma(t_T)=t_U\), and therefore
\[
\sigma\bigl(k[t_T]_{(t_T)}\bigr)=k[t_U]_{(t_U)}.
\]
Integrality is preserved by field isomorphisms, so
\[
\sigma(\mathcal O_T)=\mathcal O_U.
\]
Because \(\sigma\) fixes \(\mathbb A_{>0}\) pointwise, applying \(\sigma\) to the defining formula for \(P_T\) gives
\[
\sigma(P_T)=P_U.
\]
This proves transitivity.

### 2. Cardinality of the family

A transcendence basis of \(\mathbb R/\mathbb Q\) has cardinality \(2^{\aleph_0}\); hence
\[
|k|=2^{\aleph_0}.
\]
For each \(c\in k\), define
\[
T_c=\pi+c\pi^2.
\]
We first check \(T_c\in X_k\). If \(c=0\), this is the transcendence of \(\pi\) over \(k\). If \(c\ne0\) and \(T_c\) were algebraic over \(k\), then \(\pi\) would be algebraic over \(k(T_c)\) from
\[
cX^2+X-T_c=0,
\]
so \(\pi\) would be algebraic over \(k\), a contradiction.

Suppose \(P_{T_c}=P_{T_d}\). By the equality criterion of Wang--Yuan--Zhang--Zhu,
\[
T_d=aT_c+b
\]
for some \(a\in\mathbb A_{>0}\) and \(b\in H_k\). Hence
\[
(d-ac)\pi^2+(1-a)\pi-b=0.
\]
The field \(H_k\) is algebraic over \(k\), while \(\pi\) is transcendental over \(k\); therefore \(\pi\) is transcendental over \(H_k\). All three coefficients above lie in \(H_k\), so they vanish. Thus
\[
a=1,\qquad b=0,\qquad d=c.
\]
Hence \(c\mapsto P_{T_c}\) is injective, giving at least continuum many distinct cones. There are at most continuum many because \(X_k\subseteq\mathbb R\). Therefore
\[
|\mathcal C_k|=2^{\aleph_0}.
\]

### 3. Continuous automorphisms cannot move a cone

Let \(\tau\) be a continuous field automorphism of \(\mathbb C\). It fixes \(\mathbb Q\). For each \(r\in\mathbb R\), choose rationals \(q_n\to r\). Continuity gives
\[
\tau(r)=\tau(\lim q_n)=\lim\tau(q_n)=\lim q_n=r.
\]
Thus \(\tau\) fixes \(\mathbb R\) pointwise. Since \(\tau(i)^2=-1\), one has \(\tau(i)=i\) or \(-i\). Hence every continuous field automorphism of \(\mathbb C\) is either the identity or complex conjugation.

Both stabilize every \(P_T\). The identity is clear. Complex conjugation fixes \(k\), \(t_T\), and \(\mathbb A_{>0}\) pointwise. The base local ring \(k[t_T]_{(t_T)}\) is therefore fixed pointwise, and its integral closure \(\mathcal O_T\) is stable under conjugation: conjugating a monic integral equation gives another monic integral equation over the same ring. Thus
\[
\overline{P_T}=P_T.
\]
Consequently, if a continuous \(\tau\) satisfies \(\tau(P_T)=P_U\), then \(P_T=P_U\). This proves the final assertion.

## Interpretation

The source paper classifies **equality** of its cones for fixed \(k\). The theorem above gives the complementary **isomorphism** classification: after forgetting the chosen embedding of the cone into the standard complex field, the entire family becomes a single ordered-field isomorphism class. The equality classification remains highly nontrivial because the conjugating automorphisms between distinct cones are necessarily discontinuous in the ordinary complex topology.

The mechanism is algebraic rather than analytic. Every real generator \(T\in X_k\) is a transcendence generator of the one-variable extension up to algebraic closure, and the cone construction is functorial under automorphisms fixing \(k\overline{\mathbb Q}\).

## Limitations

The theorem concerns only the explicit family \(\mathcal C_k\) of Wang--Yuan--Zhang--Zhu for one fixed coefficient field \(k\). It does not classify all compatible directed orders on \(\mathbb C\), nor does it resolve the Birkhoff--Pierce lattice-order problem. The automorphisms furnished by algebraic-closure extension are nonconstructive, and for distinct cones the final part shows they cannot be continuous in the usual topology.

Originality is asserted only to the best of our knowledge. The conjugacy argument is short once the source construction and the standard extension theorem for algebraic closures are combined, so independent prior or contemporaneous observation is a material residual risk.

## References

1. Wenyi Wang, Ruisong Yuan, Yuehui Zhang, Yuhang Zhu, *Directed partial orders on the complex number field*, arXiv:2609.20494v1 (2026). https://arxiv.org/abs/2609.20494
2. The Stacks Project, Section 9.10, especially Lemmas 9.10.5--9.10.6 on embeddings into and uniqueness of algebraic closures. https://stacks.math.columbia.edu/tag/09GP
3. Niels Schwartz and YiChuan Yang, *Bi-Condition of Existence for a Compatible Directed Order on an Arbitrary Field*, Symmetry 15 (2023), 215. https://doi.org/10.3390/sym15010215
