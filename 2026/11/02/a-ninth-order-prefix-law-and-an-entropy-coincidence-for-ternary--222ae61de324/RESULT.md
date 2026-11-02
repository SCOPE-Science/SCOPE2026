# A ninth-order prefix law and an entropy coincidence for ternary multiplier \(85\)

## Finding
Let
\[
\Sigma=\left\{\sum_{j\ge0}a_j3^j:a_j\in\{0,1\}\right\}\subseteq\mathbb Z_3,
\qquad X_M=\Sigma\cap M^{-1}\Sigma.
\]
For \(n\ge0\), let \(a_M(n)\) count the distinct length-\(n\) low-order ternary prefixes extendible to members of \(X_M\), with \(a_M(0)=1\). For the sparse ternary multiplier \(85=(10011)_3=3^4+4\), the complete prefix-count generating function is
\[
\boxed{\sum_{n\ge0}a_{85}(n)z^n=
\frac{1+z+z^2+2z^3+3z^4+2z^5+3z^6+z^7+z^8}
{1-z-z^5-2z^7-z^9}.}
\]
Consequently the counts satisfy, for every \(n\ge9\),
\[
\boxed{a_{85}(n)=a_{85}(n-1)+a_{85}(n-5)+2a_{85}(n-7)+a_{85}(n-9),}
\]
with the first nine counts \((1,2,3,5,8,11,16,22,32)\). Despite the distinct prefix languages and graph sizes,
\[
\boxed{\dim_H X_{85}=\dim_H X_{13}=\log_3\beta\approx0.347934,}
\]
where \(\beta\) is the unique real root greater than one of \(t^3-t^2-1=0\). The carry graph for \(85\) has \(18\) reachable states and \(24\) edges, while that for \(13\) has \(3\) states and \(4\) edges. Their level-three counts are respectively \(5\) and \(4\).

## Assumptions and scope
The statements concern the ordinary \(3\)-adic metric on \(\mathbb Z_3\) and prefixes read from the least significant ternary digit. Only multipliers \(M=13\) and \(M=85\) are classified; no assertion is made for all \(M=3^k+4\). The dimension uses normalized \(3\)-adic Hausdorff dimension. Multiplication by either multiplier is a \(3\)-adic unit operation.

## Proof
Write a candidate input as \(x=\sum_{j\ge0}a_j3^j\). If the current multiplication carry is \(c\ge0\) and the next input digit is \(a\in\{0,1\}\), put \(u=c+Ma\). The output digit is \(u\bmod3\). An edge labeled \(a\) is allowed if and only if this digit is \(0\) or \(1\), and then the new carry is \(\lfloor u/3\rfloor\). Starting at carry zero, this gives a deterministic, right-resolving graph. Its carries are bounded by \(\lfloor M/2\rfloor\), so breadth-first enumeration terminates; all enumerated states have an outgoing edge, so all finite paths extend indefinitely.

For \(M=85\), exhaustive carry enumeration gives exactly the states
\[
\{0,1,3,4,9,10,11,13,14,28,29,31,32,33,38,39,41,42\}
\]
and \(24\) digit-labeled edges. For \(M=13\), the states are \(\{0,1,4\}\), with \(4\) edges. Let \(A_M\) be each graph's adjacency matrix, and \(\mathbf1\) the all-ones column vector. The vector \(v_n=A_M^n\mathbf1\) counts extendible paths of length \(n\) from each state, and \(a_M(n)\) is its coordinate at carry zero. Direct exact integer evaluation of the finitely specified transition rule gives the **statewise** identities
\[
(A_{85}^9-A_{85}^8-A_{85}^4-2A_{85}^2-I)\mathbf1=0,
\qquad (A_{13}^3-A_{13}^2-I)\mathbf1=0.
\]
Multiplying each identity by further powers of its adjacency matrix proves the displayed recurrences for **every** subsequent length. The first nine carry-zero counts for \(85\) are
\[
1,2,3,5,8,11,16,22,32.
\]
Multiplying their generating series by the recurrence polynomial \(1-z-z^5-2z^7-z^9\) gives the displayed numerator, with all later coefficients zero. Likewise for \(13\), the first counts are \(1,2,3\), giving
\[
\sum_{n\ge0}a_{13}(n)z^n=\frac{1+z+z^2}{1-z-z^3}.
\]
Finally, the denominator for \(85\) factors exactly as
\[
1-z-z^5-2z^7-z^9=(1-z-z^3)(1+z^3+z^4+z^6).
\]
The second factor is strictly positive for positive real \(z\), while \(1-z-z^3\) has a unique zero \(r\in(0,1)\). Both generating functions have nonnegative coefficients and a genuine simple pole at \(r\), because their numerators are strictly positive there. By Pringsheim's theorem, their radii of convergence equal \(r\): a smaller radius would force another positive-real singularity. Thus both prefix counts have exponential growth rate \(\beta=r^{-1}\), where \(\beta^3-\beta^2-1=0\). The established dimension formula for right-resolving \(3\)-adic path sets identifies their Hausdorff dimensions with \(\log_3\beta\). The counts at length three prove their prefix languages are not identical.

## Verification
The accompanying standalone program `verify_85.py` reconstructs both graphs by exhaustive breadth-first carry enumeration, checks all \(18\) and \(3\) state values of the two vector-polynomial identities, independently enumerates allowed input-digit prefixes at depths \(0\) through \(11\), and checks the numerator and denominator arithmetic using exact integers. Its output terminates in `VERIFY_OK`. These finite identities are certificates for all depths because the vector identities can be multiplied by any nonnegative power of the corresponding adjacency matrices.

## Relationship to prior work
Abram and Lagarias [1] proved the general construction of finite right-resolving carry automata and the dimension formula, and gave explicit examples and infinite families, including the already-known growth constant \(\beta\) for multiplier \(13\) as the \(L_3\) case, and independently for multiplier \(19\). These general methods and previously published examples are not claimed as new. The precise new claim is the specialized all-depth recurrence/generating function for the distinct sparse multiplier \(85\) and its exact entropy coincidence with \(13\), despite different prefix languages and graph sizes. Their 2015 sequel [2] develops further infinite families. The historical-priority search did not identify a prior explicit treatment of the stated \(85\) law; its full-text overlap with the sequel has not been conclusively excluded.

## Limitations
This does not classify an infinite family of sparse multipliers, nor does it establish a new general automaton-construction principle. A finite computation of one graph is sufficient here only because an exact statewise matrix identity is shown; a finite list of initial prefix counts alone would not prove the recurrence. The source comparison cannot establish absolute historical uniqueness and remains subject to independent literature review. Independent mathematical audit has not been performed.

## References
[1] William C. Abram and Jeffrey C. Lagarias, *Intersections of multiplicative translates of 3-adic Cantor sets*, arXiv:1308.3133 (first publicly posted 2013-08-14); *J. Fractal Geometry* 1 (2014), 349–390, DOI:10.4171/JFG/11, Sections 2, 4, 5.

[2] William C. Abram, Artem Bolshakov, and Jeffrey C. Lagarias, *Intersections of multiplicative translates of 3-adic Cantor sets II: two infinite families*, arXiv:1508.05967 (first publicly posted 2015-08-24); subsequently *Experimental Mathematics* 26 (2017), 468–489.
