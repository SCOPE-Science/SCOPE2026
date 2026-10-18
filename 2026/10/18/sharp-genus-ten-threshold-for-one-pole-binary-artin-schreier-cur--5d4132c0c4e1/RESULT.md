# Sharp genus-ten threshold for one-pole binary Artin–Schreier curves without degree-six places

## Finding
Let \(C_f\) be the smooth projective completion over \(\mathbf F_2\) of
\[
y^2+y=f(x),\qquad f\in\mathbf F_2[x],\quad \deg(f)=2g+1\text{ odd}.
\]
Then \(C_f\) has genus \(g\). Among this natural family (curves whose Artin–Schreier map has its only pole over infinity), the **smallest genus for which a curve has no closed point of degree six is exactly ten**. More precisely, every such curve with \(g\le9\) possesses a degree-six closed point, whereas
\[
C:\quad y^2+y=x^{21}+x^7
\]
is smooth of genus ten and has **no** degree-six closed point. The assertion is limited to the one-pole polynomial Artin–Schreier family; it is not a minimum-genus claim for arbitrary curves or arbitrary hyperelliptic covers.

## Assumptions and scope
The ground field is \(\mathbf F_2\). All points mean closed points of the smooth complete geometric curve over this ground field. The polynomial has odd leading degree, so its Artin–Schreier extension has a single ramified place, infinity, and its genus is \(g=(\deg f-1)/2\). The extension is geometrically connected because an odd-degree polynomial cannot equal \(h^2+h\) plus a constant for a polynomial/rational function \(h\). A degree-six base place on \(\mathbf P^1\) splits into two degree-six places above it if its absolute trace of \(f\) is zero; if the trace is one, it gives one degree-twelve place. A degree-three base place contributes a degree-six place precisely when its trace is one. All finite base places are unramified.

## Proof
Let \(K=\mathbf F_2[t]/(t^6+t+1)\), with the image of \(t\) encoded as the integer \(2\) and field elements encoded as six-bit coefficient vectors. The irreducibility of the displayed sextic is checked using polynomial modular arithmetic (or by the fact that its root has multiplicative order \(63\)). Write \(\operatorname{Tr}\) for the absolute trace \(K\to\mathbf F_2\).

The nine Frobenius orbits of field elements of exact degree six have representatives, in the stated coefficient encoding,
\[
2,3,6,7,32,33,34,40,41.
\]
The two orbits of exact degree three have representatives \(14,15\). These exhaust the places of these degrees on the affine line, since there are nine and two respectively. For a polynomial \(f\), absence of degree-six points on \(C_f\) therefore means **simultaneously**
\[
\operatorname{Tr}(f(a))=1\quad\text{at all nine degree-six representatives},
\]
and trace zero at both degree-three representatives (using the trace to their degree-three field, equivalently half the indicated six-fold trace; the latter is always zero for degree-three elements and is not used as a surrogate for the degree-three trace). The ramified point above infinity has degree one.

Here is an exact *dual obstruction*, requiring no exhaustive search over curve equations. For the seven degree-six representatives
\[
S=\{3,6,7,32,33,34,40\},
\]
direct arithmetic in \(K\) gives
\[
\sum_{a\in S}\operatorname{Tr}(a^j)=0\quad (0\le j\le20),
\qquad \sum_{a\in S}\operatorname{Tr}(a^{21})=1.
\]
Thus, for **every** \(f\in\mathbf F_2[x]\) of degree at most twenty, the sum \(\sum_{a\in S}\operatorname{Tr}(f(a))\) equals zero. But a curve with no degree-six closed point would require each of these seven traces to be one, giving sum one in \(\mathbf F_2\), a contradiction. This proves nonexistence for all odd degrees at most nineteen, hence every \(g\le9\).

For the sharp witness \(f=x^{21}+x^7\), exact field arithmetic gives absolute trace one at **all nine** degree-six representatives and degree-three trace zero at both degree-three representatives. Indeed, on degree-three elements one has \(a^7=1\) when \(a\ne0\), so \(f(a)=a^{21}+a^7=0\). Consequently there are no degree-six places upstairs. For an independent cross-check, the numbers of rational points on the curve over extension degrees \(1,2,3,6\) are respectively \(5,5,17,17\). By Möbius inversion, its number of degree-six places equals
\[
B_6(C)=\frac{N_6-N_3-N_2+N_1}{6}=0.
\]
Because the polynomial has leading odd degree \(21\), the smooth model has genus \(10\), and the bound is attained.

## Verification
Run `python3 verify_onepole.py` with Python 3. The standalone standard-library program constructs the field \(K\) with exact six-bit polynomial arithmetic, confirms the degree-three and degree-six Frobenius orbits, checks each of the twenty-two parity identities in the dual certificate, verifies all eleven trace conditions for the witness, counts points over four field extensions and checks the degree-six Möbius formula. All checks passed from the packaged file. The proof uses the finite-field certificate for finite exact identities, and Artin–Schreier splitting and genus theory for statements about all curves in the specified family.

## Relationship to prior work
Aubry–Herbaut–Monaldi (arXiv:2310.11218) define the least degree above which all genus-\(g\) curves over \(\mathbf F_q\) have closed points; they determine this invariant for genera one, two and three and provide general upper bounds. Their statements do not assert the sharp minimum genus ten within this one-pole family for absence of degree-six places. Xarles's 2020 complete genus-four census provides equations and zeta information for genus four; its finite-genus database neither supplies the present genus-ten witness nor excludes genus-five through genus-nine one-pole curves via the seven-orbit dual obstruction. The issue is a restricted-family, sharp geometric threshold rather than a claim about the unrestricted invariant.

## Limitations
No claim is made that ten is the minimum genus among *all* smooth curves, all hyperelliptic curves, or all Artin–Schreier covers with multiple poles. An independent mathematical audit is not performed here. Equivalent trace-code duality arguments may exist under a different name; an indexed-source search cannot establish publication priority.

## References
- Y. Aubry, F. Herbaut and J. Monaldi, “Closed points on curves over finite fields,” arXiv:2310.11218 (first public October 17, 2023).
- X. Xarles, “A census of all genus 4 curves over the field with 2 elements,” arXiv:2007.07822 (2020), for comparison with the distinct genus-four census question.
- Standard Artin–Schreier theory of cyclic covers in characteristic two (genus and splitting via the absolute trace).
