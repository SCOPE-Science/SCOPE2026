# Exact zeta function and Jacobian isogeny profile of a genus-nine extremal curve

## Finding
Let \(C\) denote the **smooth projective normalization over \(\mathbb F_2\)** of the affine plane curve
\[
(x^7+x)(z^4+z)=x^8+x^6+x^4+x^2+1.
\]
Its genus is \(9\). Its zeta function is
\[
Z(C/\mathbb F_2,T)=\frac{P_C(T)}{(1-T)(1-2T)},\quad
P_C(T)=(1-T+2T^2)(1+T+2T^2)^2(1-T^2+4T^4)(1-2T^2+T^4-8T^6+16T^8).
\]
Consequently \(\#\operatorname{Jac}(C)(\mathbb F_2)=P_C(1)=1024\). The four displayed rationally irreducible factors have degrees \(2,2,4,8\), so the Jacobian is \(\mathbb F_2\)-isogenous to a product of one elliptic factor of trace \(1\), two elliptic factors of trace \(-1\), one simple abelian surface, and one simple abelian fourfold. No polarization-compatible decomposition is claimed.

## Assumptions and scope
All points are counted on the smooth projective curve, not naively on a possibly singular projective closure of the displayed plane model. The ground field is \(\mathbb F_2\), and its degree-\(n\) extension is \(\mathbb F_{2^n}\) for positive integers \(n\). Tafazolian, Proposition 7.2 of arXiv:2609.14830v1, identifies the equation as a genus-nine ordinary curve and as the degree-two Artin–Schreier cover of the elliptic curve
\[
E:\quad y^2+xy=x^3+1,\qquad w^2+w=f,\qquad
f=\frac{y}{x}+\frac{x^4+x^3+1}{x^4+x}.
\]
In the same proposition, the polar divisor of \(f\) comprises precisely the eight simple poles at \(E[8]=E(\mathbb F_4)\). This is essential input for the correction from affine to projective counts.

## Proof
**Step 1: Account for all missing points.** Every simple pole of an Artin–Schreier function in characteristic two is totally ramified, with exactly one point above it and unchanged residue field. Here the polar set is
\[
\{O,(0,1)\}\cup\{(a,0),(a,a):a\in\mathbb F_4^\times\}.
\]
Its points rational over \(\mathbb F_{2^n}\) number \(r_n=4\) for odd \(n\), and \(r_n=8\) for even \(n\). Away from those poles, the substitutions proved in Tafazolian's Proposition 7.2 identify the affine plane model with the cover's affine complement. Indeed, the coefficient \(x^7+x=x(x^3+1)^2\) can vanish only at \(x=0\) or at \(x\in\mathbb F_4^\times\). At \(x=0\) the right side of the equation equals \(1\); at \(x^3=1\) it equals \(x\ne0\). Therefore no plane affine solution lies at these excluded coordinates, and all omissions are exactly the poles just counted.

**Step 2: A finite-field point-count formula.** Define
\[
A_n=\#\{(x,z)\in\mathbb F_{2^n}^2:(x^7+x)(z^4+z)=x^8+x^6+x^4+x^2+1\}.
\]
Then the geometric argument gives the exact identity
\[
\#C(\mathbb F_{2^n})=A_n+r_n,\qquad r_n=\begin{cases}4&n\text{ odd},\\8&n\text{ even}.\end{cases}
\]
For \(a=x^7+x\ne0\), the number of admissible \(z\) is the size of the fiber of the \(\mathbb F_2\)-linear map \(z\mapsto z^4+z\) over the explicitly computed element \((x^8+x^6+x^4+x^2+1)/a\). Enumerating every \(x,z\) in the complete finite field for each \(1\le n\le9\), with irreducibility-checked field moduli, yields
\[
(A_1,\ldots,A_9)=(0,0,0,16,40,0,112,304,504),
\]
and therefore
\[
(N_1,\ldots,N_9)=(4,8,4,24,44,8,116,312,508),\quad N_n=\#C(\mathbb F_{2^n}).
\]
The finite exhaustion is rigorous because each complete field is represented by exactly its \(2^n\) residues modulo a separately checked irreducible binary polynomial. The accompanying executable also independently counts the same smooth-curve points from \(E\) using the trace-zero criterion for \(w^2+w=f\) away from the poles, with one ramified point at each rational pole. Every count agrees.

**Step 3: Recover the entire numerator, not merely nine sample values.** Write \(P_C(T)=\sum_{j=0}^{18}c_jT^j\), with \(c_0=1\), and set \(S_n=2^n+1-N_n\). The zeta logarithmic derivative gives Newton's identity
\[
jc_j=-\sum_{i=1}^{j}c_{j-i}S_i\quad(1\le j\le9).
\]
It yields
\[
(c_0,c_1,\ldots,c_9)=(1,1,2,0,2,2,-4,-8,-11,5).
\]
For a smooth projective genus-nine curve over \(\mathbb F_2\), the Hasse–Weil functional equation forces
\[
c_{18-j}=2^{9-j}c_j\quad(0\le j\le9).
\]
The resulting degree-eighteen polynomial has coefficient sequence
\[
(1,1,2,0,2,2,-4,-8,-11,5,-22,-32,-32,32,64,0,256,256,512),
\]
which expands to the factored polynomial in the finding. Each of its four displayed distinct factors is irreducible over \(\mathbb Q\), as may be checked by standard polynomial gcd and rational factor algorithms. Honda–Tate theory and semisimplicity of finite-field isogeny categories give the stated isogeny decomposition; the repeated quadratic contributes multiplicity two. Evaluation at \(T=1\) gives \(1024\).

## Verification
Run \(\texttt{python3 check_zeta.py}\). Its self-contained binary finite-field implementation verifies the irreducibility of all nine field moduli, enumerates both the affine plane fibers and the elliptic Artin–Schreier cover, constructs the zeta coefficients by Newton identities and the functional equation, checks the complete factorization and \(P_C(1)\), and prints \(\texttt{NAKAJIMA_GENUS_NINE_ZETA_EXACT_OK}\). A separate check over \(\mathbb F_{2^{10}}\) gives \(808\) points, matching the predicted tenth power sum; that additional check is not required for the complete degree-eighteen determination. The key eight-pole and genus input comes from the cited primary article, not the finite search.

## Relationship to prior work
Tafazolian's 2026 paper gives the precise curve, genus, ramification, and automorphism group, but does not state this zeta numerator, Jacobian factorization, or all extension-field point counts. The earlier Giulietti–Korchmáros genus-nine construction cited there has a distinct displayed equation with coefficients in \(\mathbb F_{16}\); it does not, without an additional identification and arithmetic calculation, determine this curve's zeta function over \(\mathbb F_2\). The general Hasse–Weil functional equation, Artin–Schreier trace criterion, and Honda–Tate isogeny theory are standard input and are not claimed as new. The contribution is the complete exact arithmetic evaluation for the explicitly motivated genus-nine base-field model.

## Limitations
This finding makes no claim for other parameter values in the extremal Artin–Schreier family, for other characteristic-two curves of genus nine, or for the abstract group structure of \(\operatorname{Jac}(C)(\mathbb F_2)\). The isogeny decomposition is over \(\mathbb F_2\), not an isomorphism of principally polarized abelian varieties. Exact historical uniqueness of this particular polynomial is not established by literature searches, and independent audit remains outstanding. The equations and residue-field correction are essential: raw affine point counts alone do not yield the stated result.

## References
1. S. Tafazolian, *Nakajima-extremal Artin–Schreier covers of ordinary elliptic curves in characteristic 2*, arXiv:2609.14830v1 (first posted 13 September 2026), Proposition 7.2, https://arxiv.org/html/2609.14830v1.
2. M. Giulietti and G. Korchmáros, *Algebraic curves with a large non-tame automorphism group fixing no point*, Transactions of the American Mathematical Society 362 (2010), 5983–6001, DOI:10.1090/S0002-9947-2010-05025-1, as discussed in reference 1, Sections 1 and 5.8.
3. Hasse–Weil zeta-function functional equation and Honda–Tate finite-field isogeny classification (standard background; used only in their established forms).
