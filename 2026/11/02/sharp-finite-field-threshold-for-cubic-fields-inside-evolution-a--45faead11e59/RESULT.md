# Sharp finite-field threshold for cubic fields inside evolution algebras

## Finding

For each prime power \(q\), regard \(L=\mathbb F_{q^3}\) as a three-dimensional commutative associative algebra over \(K=\mathbb F_q\). An **evolution algebra** over \(K\) is a (possibly nonassociative) commutative algebra with a basis in which distinct basis elements have zero product. Define \(\operatorname{edim}_K(L)\) as the least dimension of an evolution algebra over \(K\) containing \(L\) as a subalgebra. Then

\[
\boxed{\operatorname{edim}_{\mathbb F_q}(\mathbb F_{q^3})=\begin{cases}6,&q\in\{2,3\},\\5,&q\ge4.\end{cases}}
\]

In both cases the optimal embedding can be chosen with its image an **ideal** of the ambient evolution algebra. Thus the cubic fields \(\mathbb F_8\) and \(\mathbb F_{27}\) attain the universal dimension-six bound for three-dimensional commutative algebras, answering the existence part of a published sharpness question in dimension three. For other finite base fields, cubic extensions have minimal ambient evolution dimension five.

## Assumptions and scope

All vector spaces, products and dimensions are over \(K=\mathbb F_q\). Fields may have characteristic two or three. An embedding is an injective \(K\)-algebra homomorphism, with no requirement that the ambient evolution algebra have an identity or be associative. The source \(L\) is the full cubic field extension; no claim is made for all three-dimensional commutative algebras or for all degrees of field extensions. We use the standard convention that a natural basis of an evolution algebra has pairwise-zero distinct products.

## Proof

### Step 1: A universal six-dimensional ideal envelope

More generally let \(A\) be any three-dimensional commutative \(K\)-algebra with basis \(a_0,a_1,a_2\). Form an evolution algebra \(E\) with natural basis \(f_{ij}\), \(0\le i\le j\le2\), and zero mixed natural-basis products. Define a linear injection \(\phi:A\to E\) by

\[
\phi(a_i)=\sum_{j=0}^{2}f_{\min(i,j),\max(i,j)}.
\]

Injectivity follows from the three independent diagonal coordinates \(f_{00},f_{11},f_{22}\). Specify the squares in \(E\) by

\[
 f_{ij}^2=\phi(a_i a_j)\quad(i<j),\qquad
 f_{ii}^2=\phi\left(a_i^2-\sum_{j\ne i}a_i a_j\right).
\]

For \(i<j\), the only common natural coordinate of \(\phi(a_i)\) and \(\phi(a_j)\) is \(f_{ij}\), so \(\phi(a_i)\phi(a_j)=\phi(a_i a_j)\). The chosen diagonal squares give \(\phi(a_i)^2=\phi(a_i^2)\). Bilinearity proves that \(\phi\) is an algebra embedding. All basis squares lie in \(\phi(A)\), hence \(E\phi(A)\subseteq\phi(A)\); the image is an ideal. This supplies \(\operatorname{edim}_K(A)\le6\) in every characteristic.

### Step 2: The off-diagonal obstruction for ambient dimension at most five

Let \(L\) be any degree-three field extension and suppose that \(\phi:L\hookrightarrow E\) is an embedding into an \(m\)-dimensional evolution algebra. Select a natural basis of \(E\). The three-dimensional subspace \(\phi(L)\subseteq E\) has three pivot coordinates; after permuting the natural basis and choosing a basis \(b_1,b_2,b_3\) of \(L\), the embedding has the coordinate form

\[
 \phi(b_i)=e_i+\sum_{\nu=1}^{m-3}\beta_{\nu i}f_\nu,
 \qquad i=1,2,3.
\]

Here all \(e_i\) and \(f_\nu\) belong to one natural basis of \(E\); their pairwise mixed products vanish. For distinct \(i,j\), therefore,

\[
 \phi(b_i b_j)=\sum_{\nu=1}^{m-3}\beta_{\nu i}\beta_{\nu j} f_\nu^2.
\]

Choose any \(K\)-linear retraction \(\pi:E\to L\) satisfying \(\pi\phi=\operatorname{id}_L\), and put \(v_\nu=\pi(f_\nu^2)\). We obtain three simultaneous identities

\[
 (b_1b_2,b_1b_3,b_2b_3)
 =\sum_{\nu=1}^{m-3}v_\nu\,
 (\beta_{\nu1}\beta_{\nu2},\beta_{\nu1}\beta_{\nu3},\beta_{\nu2}\beta_{\nu3}).\tag{1}
\]

For any basis \(b_1,b_2,b_3\) of the field, the three cross products are nonzero and any two are linearly independent over \(K\): a proposed dependence cancels a common nonzero field factor and contradicts linear independence of two basis elements. In particular the rank of the three cross products is either two or three. Formula (1) implies \(m-3\ge2\), giving the lower bound \(m\ge5\) over every base field.

### Step 3: Why base fields with two or three elements require six dimensions

Suppose for contradiction that \(m=5\). Then (1) expresses the cross-product triple as a sum of at most two off-diagonal rank-one patterns

\[
 p(a,b,c)=(ab,ac,bc)\in K^3.
\]

Its rank is at most two. Consequently the cross products have rank exactly two and possess a unique relation up to scalar,

\[
 r_1 b_1b_2+r_2 b_1b_3+r_3 b_2b_3=0.
\]

Each coefficient \(r_i\) is nonzero, because any two cross products are independent. Let \(W=\{(z_1,z_2,z_3):r_1z_1+r_2z_2+r_3z_3=0\}\), a two-dimensional plane. Because the cross-product triple has rank two, the two patterns in (1) must be nonzero, independent, and both lie in \(W\).

We now count all projective nonzero patterns lying in \(W\). If any of \(a,b,c\) vanishes, at most one coordinate of \(p(a,b,c)\) is nonzero, impossible since all \(r_i\ne0\). Thus \(a,b,c\ne0\); scale to \(a=1\) and write \(b=u\in K^\times\). The plane equation forces

\[
 c=-\frac{r_1u}{r_2+r_3u}.
\]

A nonzero solution exists for exactly the \(q-2\) choices

\[
 u\in K^\times\setminus\{-r_2/r_3\}.
\]

Different choices give different projective patterns because the ratio of the second and third pattern coordinates equals \(1/u\). Therefore \(W\) contains precisely \(q-2\) projective directions of the form \(p(a,b,c)\). For \(q=2\), it has none; for \(q=3\), it has only one. Neither field admits two independent such patterns. This contradicts (1) when \(m=5\). The universal six-dimensional construction then proves

\[
\operatorname{edim}_{\mathbb F_2}(\mathbb F_8)=
\operatorname{edim}_{\mathbb F_3}(\mathbb F_{27})=6.
\]

### Step 4: Explicit five-dimensional ideal envelopes for every \(q\ge4\)

Choose \(t\in L\) generating the cubic extension \(L/K\), and put \(z=t/(t-1)\). The elements \(b_1=1,b_2=t,b_3=z\) form a basis. Indeed, a relation \(z=\alpha+\beta t\) over \(K\) would yield a nonzero polynomial of degree at most two annihilating \(t\). Their mixed products satisfy

\[
 b_1b_2=t,\quad b_1b_3=z,\quad b_2b_3=tz=t+z.\tag{2}
\]

Because \(q\ge4\), choose distinct \(u,v\in K\setminus\{0,1\}\), and set \(d_w=w/(w-1)\) for \(w=u,v\). The two patterns

\[
 p_w=(w,d_w,wd_w)
\]

lie in the plane \(z_1+z_2-z_3=0\). Their first two coordinates are linearly independent since

\[
 u d_v-vd_u=\frac{uv(u-v)}{(u-1)(v-1)}\ne0.
\]

Consequently unique \(V_u,V_v\in L\) satisfy

\[
 t=uV_u+vV_v,\qquad z=d_uV_u+d_vV_v.
\]

As \(wd_w=w+d_w\), equation (2) also gives \(tz=ud_uV_u+vd_vV_v\). Define the evolution algebra \(E\) with five natural basis vectors \(e_1,e_2,e_3,f_u,f_v\), pairwise distinct products zero. Let

\[
 (\beta_{u1},\beta_{u2},\beta_{u3})=(1,u,d_u),\quad
 (\beta_{v1},\beta_{v2},\beta_{v3})=(1,v,d_v),
\]

and define the injective linear map

\[
 \phi(b_i)=e_i+\beta_{ui}f_u+\beta_{vi}f_v.
\]

Set

\[
 f_u^2=\phi(V_u),\quad f_v^2=\phi(V_v),\qquad
 e_i^2=\phi(b_i^2-\beta_{ui}^{2}V_u-\beta_{vi}^{2}V_v).
\]

For distinct \(i,j\), (2) and the mixed-product representation yield \(\phi(b_i)\phi(b_j)=\phi(b_ib_j)\). The diagonal-square definition gives \(\phi(b_i)^2=\phi(b_i^2)\). Thus \(\phi\) embeds the cubic field as a subalgebra. Every natural basis square is in \(\phi(L)\), hence its image is an ideal. The universal lower bound five from Step 2 proves optimality.

## Verification

Two standalone Python programs use polynomial finite-field arithmetic and exact integral enumeration. `verify_f8_envelope.py` exhausts all \(168\) ordered bases of \(\mathbb F_8\) over \(\mathbb F_2\), checks that no two-term off-diagonal decomposition exists, and validates every multiplication/ideal condition in an explicit six-dimensional envelope. `verify_cubic_field_phase.py` exhausts all \(11232\) ordered bases of \(\mathbb F_{27}\) over \(\mathbb F_3\), checks the allowed off-diagonal pattern directions for every normal with nonzero coefficients, and constructs and verifies the five-dimensional ideal envelope of \(\mathbb F_{64}\) over \(\mathbb F_4\). Both return `VERIFY_OK`. These tests corroborate but do not replace the symbolic proof for all prime powers.

## Relationship to prior work

Costoya, Fernández Ouaridi and Viruel establish a universal evolution-envelope upper bound \(n(n+1)/2\) for commutative algebras and ask whether it is sharp (Question 3.7 in their September 2026 preprint). Their Theorem 3.5 supplies a relevant criterion for reduced dimensions. Kaygorodov, Martín González and Viruel repeat the sharpness question as Question 42 in their October 2026 survey. The present finding resolves the existence question in dimension three through the cubic fields over \(\mathbb F_2\) and \(\mathbb F_3\), and provides an exact field-size threshold in this natural extension-field family. A known result on \(K\oplus V\) with square-zero radical concerns non-field local algebras and does not imply the cubic-field theorem. We do not claim to resolve the universal sharpness question in every dimension or for every base field.

## Limitations

Only cubic **finite** field extensions are classified. The proof does not classify optimal envelopes up to isomorphism or determine minimal ambient dimensions of arbitrary three-dimensional algebras. The construction proves ideal embeddings but does not assert that every possible embedding is ideal. Exhaustive computer checks are limited to the explicitly stated finite fields; universality rests on Steps 1–4. A fully independent mathematical audit and a conclusive historical-priority review remain outstanding.

## References

1. C. Costoya, M. Fernández Ouaridi, and A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784 (first public version September 26, 2026), https://arxiv.org/abs/2609.32784 ; Theorem 2.1, Theorem 3.5, Question 3.7.
2. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first public version October 15, 2026), https://arxiv.org/abs/2610.22248 ; Question 42.
