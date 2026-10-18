# Two-conic blocking pairs: one orbit over \(\mathbf F_5\), none over \(\mathbf F_7\)

## Finding
Let \(q\in\{5,7\}\), and let \(C_1,C_2\subset\mathbf P^2_{\mathbf F_q}\) be two distinct geometrically smooth conics. Call the unordered pair *blocking* if \((C_1\cup C_2)(\mathbf F_q)\) meets every \(\mathbf F_q\)-line. Over \(\mathbf F_5\) there are exactly **18,600** blocking unordered pairs, and they form **one orbit** under \(\operatorname{PGL}_3(\mathbf F_5)\), with stabilizer of order **20**. Each pair intersects in exactly one rational point, giving an eleven-point blocking set with rational line-intersection spectrum \((t_0,t_1,t_2,t_3,t_4,t_5,t_6)=(0,11,10,5,5,0,0)\). Over \(\mathbf F_7\), **no** pair of geometrically smooth conics has a blocking rational union. The statement concerns these two fields only; it does **not** establish nonexistence over every larger finite field.

## Assumptions and scope
A conic is the zero divisor of a nonzero homogeneous quadratic in three variables, up to nonzero scalar. In odd characteristic, geometric smoothness is equivalent to the determinant of the symmetric polar matrix being nonzero. Every smooth conic over a finite field is projectively equivalent to \(C_0: XZ-Y^2=0\). An unordered pair is counted once regardless of its ordering. The blocking property uses only rational points and all rational lines; geometric smoothness is assessed over the algebraic closure. No smooth or irreducible union is claimed: the union has two distinct smooth components.

## Proof
For \(q=5\) or \(7\), normalize each nonzero coefficient vector \((a,b,c,d,e,f)\in\mathbf F_q^6\) to have leading nonzero coefficient one, encoding \(aX^2+bXY+cXZ+dY^2+eYZ+fZ^2\). Let
\[
H=\begin{pmatrix}2a&b&c\\b&2d&e\\c&e&2f\end{pmatrix}.
\]
The condition \(\det H\ne0\) is necessary and sufficient for geometric smoothness: its vanishing characterizes a common nonzero zero of the linear partial derivatives over the algebraic closure, which is a singular point on the conic by Euler's identity since the characteristic is odd. The number of smooth conics is \(q^5-q^2\), also independently verified by exhaustive enumeration.

Enumerate the normalized points \([X:Y:Z]\in\mathbf P^2(\mathbf F_q)\) and normalized linear forms \(\ell\) on the dual projective plane. Form the bit mask \(M(F)\) of the rational zeros of a smooth quadratic \(F\), and for each rational line the mask \(M(\ell)\). Fix \(C_0\); by projective transitivity, examining its partners exhausts every projective class of pairs. A candidate \(F\) is a blocking partner exactly when
\[
 M(F)\cap M(\ell)\ne\varnothing\quad\text{for every }\ell\text{ with }M(C_0)\cap M(\ell)=\varnothing.
\]
The supplied complete normalized-coefficient enumerator (`verify_conic_census.py`) checks this exact condition for all \(q^5-q^2\) smooth conics for each field. It obtains \(12\) partners for \(q=5\), all with one point in common with \(C_0\), and \(0\) partners for \(q=7\). Since there are \(3100\) smooth conics over \(\mathbf F_5\), double counting ordered choices of the first conic gives \(3100\cdot12/2=18{,}600\) unordered pairs.

For \(q=5\), the stabilizer of \(C_0\) is the order-\(120\) group \(\operatorname{PGL}_2(\mathbf F_5)\), acting on the Veronese coordinates \([s^2:st:t^2]\). The program `verify_conic_orbit.py` enumerates its complete binary-matrix action and shows that the twelve partner masks form one orbit. Projective transitivity on the first conic then proves there is one global unordered-pair orbit. The known order \(|\operatorname{PGL}_3(\mathbf F_5)|=372{,}000\) gives pair stabilizer \(372{,}000/18{,}600=20\). The same program evaluates every rational line against each eleven-point union to obtain the stated line spectrum. A concrete representative is
\[
 C_0:\ XZ-Y^2=0,\qquad C_1:\ X^2+2XZ+3Y^2=0\quad\text{over }\mathbf F_5.
\]
Its union has no rational line as a component: any line meets each smooth conic in at most two geometric points, so has at most four points in the rational union, fewer than the six points of a rational line.

## Verification
Run `python verify_conic_census.py` and `python verify_conic_orbit.py` using standard Python 3. For a separately implemented vectorized count, run `python crosscheck_numpy.py` (requires NumPy). The first program checks every normalized conic equation, all \(31\) or \(57\) rational points, and every corresponding rational line; the second checks the complete \(120\)-element conic-stabilizer action. The NumPy script uses matrix evaluation and an independently written determinant and incidence predicate. All three programs passed with the output counts above. No sampled point checks substitute for geometric smoothness: \(\det H\ne0\) is exact.

## Relationship to prior work
Asgarli–Ghioca–Yip, arXiv:2208.13299 (first publicly available 2022-08-28), investigates when algebraic plane curves have blocking rational point sets; its theorems on low-degree irreducible curves do not classify **unions of two smooth conics**. Al-Mukhtar–Thumai (2015) constructs blocking sets containing conics together with selected lines and extra points over \(\mathbf F_5\); the inspected construction does not supply the current unordered smooth-conic-pair classification. Coolsaet–Botteldoorn–Fack (2022) classifies minimal blocking point sets in small projective planes; that point-set census does not, by itself, classify decompositions into smooth conics or establish the two-conic exclusion. The 2005–2006 Aguglia–Korchmáros results concern minimum blockers of conic external or nonsecant lines; they are relevant but their abstracts do not decide the asserted non-minimum conic-partner incidence. All these comparators are distinguished by their *statements* and not only their titles.

## Limitations
This is an exact two-field finite result, not a theorem for all \(q\ge7\) or for arbitrary reducible quartics. The q=7 negative statement does not exclude blocking unions with singular conics or nonconic components, nor irreducible smooth blocking quartics. An exhaustive point-set classification for \(q\le8\) and the older conic external-line literature present residual bibliographic priority risk, especially because their complete texts were not all accessible. A self-review has been performed; independent audit has not.

## References
- S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299, version 1 publicly posted 2022-08-28; https://arxiv.org/abs/2208.13299.
- A. S. Al-Mukhtar and H. S. Thumai, *The Construction of Minimal (b,t)-Blocking Sets Containing Conics in PG(2,5) with the Complete Arcs and Projective Codes Related with Them*, Ibn Al-Haitham J. Pure Appl. Sci. 28 (2015), 163–170; https://jih.uobaghdad.edu.iq/index.php/j/article/view/198.
- K. Coolsaet, A. Botteldoorn, V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, J. Combin. Designs 30 (2022), 561–580; https://doi.org/10.1002/jcd.21842.
- A. Aguglia and G. Korchmáros, *Blocking sets of external lines to a conic in PG(2,q), q odd*, Combinatorica 26 (2006), 379–394; https://doi.org/10.1007/s00493-006-0021-2.
- A. Aguglia and G. Korchmáros, *Blocking sets of nonsecant lines to a conic in PG(2,q), q odd*, J. Combin. Designs 13 (2005), 292–301; https://doi.org/10.1002/jcd.20042.
