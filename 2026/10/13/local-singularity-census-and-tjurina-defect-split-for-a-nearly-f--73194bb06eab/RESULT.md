# Local singularity census and Tjurina-defect split for a nearly-free conic–line arrangement
## Finding
Consider the degree-nine arrangement
\[
C=V\!\bigl(x_0Q_1Q_2Q_3Q_4\bigr)\subset\mathbb P^2_{\mathbb C},
\]
where
\[
\begin{aligned}
Q_1&=x_0x_1-x_1^2+x_2^2,\\
Q_2&=x_0x_2-x_0^2+x_1^2-x_2^2,\\
Q_3&=x_0x_1+x_1^2-x_2^2,\\
Q_4&=x_0x_2+x_0^2-x_1^2+x_2^2.
\end{aligned}
\]
For the five singular points recorded in the source,
\[
p_1=(1:0:0),\quad p_2=(1:-1:0),\quad p_3=(1:1:0),\quad p_4=(0:-1:1),\quad p_5=(0:1:1),
\]
the local types are as follows. The point \(p_1\) is an \(A_3\) tacnode. The points \(p_2,p_3\) are ordinary triple points, hence of type \(D_4\). Each of \(p_4,p_5\) has five smooth branches, with exactly two tangent pairs of contact order two and all other branch pairs transverse. In local coordinates \(u=x_0\), \(v=x_1+1\) at \(p_4\), the tangent cone is
\[
u(u-2v)^2(u+2v)^2.
\]
The two non-quasihomogeneous germs satisfy
\[
(\mu,\tau)=(20,18),
\]
and have minimal embedded resolution with exceptional total-transform multiplicities \(5,7,7\). Their local monodromy characteristic polynomial is
\[
(t-1)(t^5-1)(t^7-1)^2.
\]
Globally,
\[
\mu(C)=51,\qquad \tau(C)=47,
\]
so the full defect \(\mu(C)-\tau(C)=4\) is the sum of two equal local defects \(20-18=2\).

## Assumptions and scope
The base field is \(\mathbb C\). The statement concerns the explicit arrangement displayed above and its five singular points. The source proves that the arrangement is nearly free with \(\operatorname{mdr}=4\), gives \(\tau(C)=47\), and detects \(p_4,p_5\) as non-quasihomogeneous by a syzygy-rank criterion. The present statement refines the local analytic/topological structure; it does not claim a classification of all nearly-free conic–line arrangements.

## Proof
Each \(Q_i\) is a smooth conic: the determinants of the four symmetric quadratic-form matrices are respectively \(-1/4,3/4,1/4,-3/4\). Hence every singularity of the reduced union comes from an intersection of distinct components.

At \(p_1\), in the chart \(x_0=1\) with \(u=x_1\), \(v=x_2\), the two incident conics have local equations
\[
-u^2+u+v^2=0,\qquad u^2+u-v^2=0.
\]
They are smooth with the same tangent \(u=0\), and their intersection ideal contains \(2u\) and then \(v^2\), so their intersection multiplicity is \(2\). Thus \(p_1\) is an \(A_3\) tacnode, with \(\mu_{p_1}=\tau_{p_1}=3\).

At \(p_2\), the three incident conics have distinct tangent lines
\[
-2u+v=0,\qquad -u=0,\qquad 2u+v=0,
\]
so \(p_2\) is an ordinary triple point, equivalently \(D_4\), with \(\mu_{p_2}=\tau_{p_2}=4\). The involution \([x_0:x_1:x_2]\mapsto[x_0:-x_1:x_2]\) preserves \(C\) and exchanges \(p_2\) with \(p_3\), so the same holds at \(p_3\).

At \(p_4\), put \(u=x_0\) and \(v=x_1+1\) in the chart \(x_2=1\). The five branch equations are
\[
\begin{aligned}
u&=0,\\
uv-u-v^2+2v&=0,\\
-u^2+u+v^2-2v&=0,\\
uv-u+v^2-2v&=0,\\
u^2+u-v^2+2v&=0.
\end{aligned}
\]
Their linear parts are \(u\), \(-u+2v\), \(u-2v\), \(-u-2v\), \(u+2v\). Thus there are three tangent directions with multiplicities \(1,2,2\). Solving the second branch for \(u\) and substituting into the third gives
\[
\frac{v^2(v-2)}{(v-1)^2},
\]
so that tangent pair has intersection multiplicity \(2\). The other tangent pair gives its negative and also has intersection multiplicity \(2\). Every remaining pair has distinct tangent lines and therefore intersection multiplicity \(1\). Hence
\[
\delta_{p_4}=2+2+8=12,
\]
and, with five branches,
\[
\mu_{p_4}=2\delta_{p_4}-5+1=20.
\]
The same involution exchanges \(p_4\) and \(p_5\), so \(\mu_{p_5}=20\) and the same branch-contact data holds there.

For the Tjurina number, let \(f(u,v)\) be the displayed local product at \(p_4\). The second singularity in this affine chart is \(p_5=(u,v)=(0,2)\). Localizing away from \(v-2\) by adjoining \(t\) and \(1-t(v-2)\), the ideal
\[
\bigl(f,f_u,f_v,1-t(v-2)\bigr)\subset\mathbb Q[t,u,v]
\]
has a lexicographic Gröbner basis whose leading monomials are
\[
t,\quad u^4,\quad u^3v,\quad u^2v^3,\quad uv^6,\quad v^8.
\]
The standard monomials therefore number
\[
8+6+3+1=18.
\]
Thus \(\tau_{p_4}=18\), and symmetry gives \(\tau_{p_5}=18\).

For the embedded resolution at \(p_4\), the first blow-up has exceptional multiplicity \(5\). Each of the two contact-two pairs meets that exceptional divisor in a separate three-component point. Blowing up those two points separates the branches, and each new exceptional divisor has multiplicity \(5+1+1=7\). The three exceptional components each have valency three in the resolved total transform. A'Campo's formula then gives
\[
\Delta_{p_4}(t)=(t-1)(t^5-1)(t^7-1)^2,
\]
and the same polynomial at \(p_5\).

Finally,
\[
\mu(C)=3+4+4+20+20=51,
\]
while
\[
\tau(C)=3+4+4+18+18=47.
\]
This reproduces the source's global Tjurina number while locating its entire four-dimensional Milnor–Tjurina defect at the two points the source identifies as non-quasihomogeneous.

## Verification
The included `verify.py` performs exact rational symbolic checks. It verifies smoothness of all four conics, the projective involution, the two affine Jacobian supports together with smoothness of the one projective point outside those charts, the tangent forms, the contact-two substitutions, the localized Gröbner basis and its \(18\)-dimensional Tjurina quotient, and the global sums \(\mu=51\), \(\tau=47\). A fresh run from the packaged file returns `VERIFY_OK`.

## Relationship to prior work
Andrade–Beorchia–Miró-Roig give this exact arrangement, list its five singular points, prove that it is nearly free with \(\operatorname{mdr}=4\) and \(\tau(C)=47\), and use their syzygy-matrix criterion to show that \(p_1,p_2,p_3\) are quasihomogeneous whereas \(p_4,p_5\) are not. They do not determine the five local singularity types, the local pairs \((\mu,\tau)\), the embedded resolution multiplicities, or the monodromy polynomial above. Their discussion also explicitly notes that the syzygy-rank criterion is set-theoretic and does not quantify \(\mu-\tau\) at a non-quasihomogeneous point.

Beorchia–Miró-Roig's earlier work on Jacobian schemes of conic–line arrangements supplies general global Tjurina and syzygy context, but does not state this local census. The closest published published-finding corpus comparison found is a different Type-II conic-pencil arrangement with four branches and one contact-two pair; its local profile does not imply the present five-branch, two-contact-pair calculation.

## Limitations
The analytic equivalence class of the two five-branch germs is not assigned a named modality class. The monodromy statement is local and follows from the displayed minimal embedded resolution. No claim is made about deformation universality or about other nearly-free degree-nine arrangements.

## References
1. A. V. Andrade, V. Beorchia, R. M. Miró-Roig, *A characterization of quasi-homogeneous singularities of free and nearly free plane curves*, arXiv:2407.05819v1, 8 July 2024, especially Example 6.1 in v1 (journal numbering differs) and the discussion of the Milnor–Tjurina defect.
2. V. Beorchia, R. M. Miró-Roig, *Jacobian schemes of conic-line arrangements and eigenschemes*, arXiv:2303.04665; Mediterr. J. Math. 21 (2024), Art. 16.
3. N. A'Campo, *La fonction zêta d'une monodromie*, Comment. Math. Helv. 50 (1975), 233–248.