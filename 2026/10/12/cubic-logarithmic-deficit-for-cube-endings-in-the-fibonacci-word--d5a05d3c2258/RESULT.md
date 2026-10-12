# Cubic logarithmic deficit for cube endings in the Fibonacci word
## Finding
Let
\[
\mathbf f=010010100100101001010010\cdots
\]
be the Fibonacci word, and let \(c_j=1\) when a cube ends at position \(j\) of \(\mathbf f\), with \(c_j=0\) otherwise.

Write \(F_0=0\), \(F_1=1\), and \(F_{m+2}=F_{m+1}+F_m\). Let \(R_L\) be the number of runs of \(1\)'s in \((c_j)_{j\ge0}\) whose starting index is smaller than \(F_{L+2}\). Then, with \(\binom ab=0\) when \(a<b\),
\[
R_L=
\binom{\lfloor L/2\rfloor}{3}
+
2\binom{\lfloor (L-1)/2\rfloor}{3}
+
\binom{\lfloor (L-2)/2\rfloor}{3}.
\]
In particular,
\[
R_L=\frac{L^3}{12}+O(L^2).
\]

Define the cube-ending deficit
\[
Z(N)=\#\{0\le j<N:c_j=0\}.
\]
If \(N\ge2\) and \(L\) is chosen by
\[
F_{L+1}\le N<F_{L+2},
\]
then
\[
R_{L-1}\le Z(N)\le 13(R_L+1).
\]
Consequently,
\[
Z(N)=\Theta((\log N)^3).
\]

Thus the exceptional prefixes of the Fibonacci word that do not end with a cube are not merely of density zero: their counting function has exact cubic polylogarithmic order.

## Assumptions and scope
The definition of a cube is a nonempty word of the form \(xxx\). Position indexing starts at \(0\), so \(c_j=1\) means that some cube is a suffix of the prefix \(\mathbf f[0\,..\,j]\).

For a nonnegative integer \(i\), \((i)_F\) denotes its canonical Zeckendorf representation. A representation of length at most \(L\) is equivalent to an integer smaller than \(F_{L+2}\).

The proof uses the published exact description of the starts of runs of \(1\)'s and the published fact that every run of \(0\)'s has length in
\[
\{1,2,3,7,8,13\}.
\]
It sharpens the published density-zero conclusion by identifying the exact cubic degree and an exact formula for one-run starts. It does not determine the exact leading constant of \(Z(N)\).

## Proof
The published run-start theorem states that a run of \(1\)'s starts at \(i\) exactly when
\[
(i)_F\in(10)^+0(0+10)(00)^*0w,
\qquad
w\in0(10)^*(\varepsilon+1).
\]

Parameterize a matching representation as follows. Write the initial \((10)^+\) as \((10)^{A+1}\) with \(A\ge0\), write \((00)^b\) with \(b\ge0\), write the repeated part of \(w\) as \((10)^c\) with \(c\ge0\), and let the final optional \(1\) be recorded by \(e\in\{0,1\}\).

There are four choices coming from the middle alternative \(0\) or \(10\) and from \(e\). If
\[
t=A+b+c,
\]
their representation lengths are respectively
\[
2t+6,\qquad 2t+7,\qquad 2t+7,\qquad 2t+8.
\]
For fixed \(t\), the number of triples \((A,b,c)\) is
\[
\binom{t+2}{2}.
\]
The decomposition is unique: the first doubled zero fixes the end of the initial \((10)^+\), the middle choice is distinguished by whether a \(1\) follows, and the remaining alternating suffix then fixes \(b,c,e\).

Summing over all \(t\) whose corresponding representation length is at most \(L\), and using
\[
\sum_{t=0}^m\binom{t+2}{2}=\binom{m+3}{3},
\]
gives
\[
R_L=
\binom{\lfloor L/2\rfloor}{3}
+
2\binom{\lfloor (L-1)/2\rfloor}{3}
+
\binom{\lfloor (L-2)/2\rfloor}{3}.
\]
The asymptotic formula \(R_L=L^3/12+O(L^2)\) follows immediately.

Now let \(F_{L+1}\le N<F_{L+2}\). Every run of \(1\)'s that starts below \(N\) has a canonical representation of length at most \(L\), so there are at most \(R_L\) such starts. The sequence begins with a run of \(0\)'s, and thereafter each run of \(0\)'s is paired with a preceding run of \(1\)'s. Therefore at most \(R_L+1\) zero-runs can meet the prefix of length \(N\). Since every zero-run has length at most \(13\),
\[
Z(N)\le13(R_L+1).
\]

For the lower bound, every run start whose representation length is at most \(L-1\) lies below \(F_{L+1}\), hence below \(N\). Each such one-run has a distinct preceding zero-run, and that zero-run contributes at least one zero before \(N\). Thus
\[
Z(N)\ge R_{L-1}.
\]

Finally, Fibonacci growth gives \(L=\Theta(\log N)\). Together with
\[
R_L=\frac{L^3}{12}+O(L^2),
\]
the two-sided bound yields
\[
Z(N)=\Theta((\log N)^3).
\]

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently constructs the regular-expression family of run-start representations and checks the exact formula for \(R_L\) through \(L=40\), including injectivity of the parameterization.

It then generates a length-\(2400\) Fibonacci prefix and decides directly from the definition whether a cube ends at every position. The resulting one-run starts are compared with the Zeckendorf regular expression, the complete zero-runs are checked against the published allowed length set, and the exact values of \(R_L\) are checked at Fibonacci cutoffs for \(6\le L\le15\).

Finally, every prefix length through \(2400\) is checked against the proved sandwich
\[
R_{L-1}\le Z(N)\le13(R_L+1).
\]

These finite checks validate the parameter bookkeeping and the direct cube predicate. The all-\(N\) theorem follows from the symbolic counting proof and the published run characterizations, not from finite extrapolation.

## Relationship to prior work
Rampersad gives an exact Fibonacci-automatic characterization of cube-ending positions. In particular, the paper characterizes the starts and lengths of the runs of \(1\)'s, proves that zero-runs have lengths \(1,2,3,7,8,13\), and proves that the density of zero positions is \(0\).

The density proof observes that the complement automaton accepts only polynomially many Zeckendorf strings of each length. It does not identify the polynomial degree, give the exact run-start counting formula above, or state a \(\Theta((\log N)^3)\) deficit law.

Shallit later studies suffixes of large Fibonacci prefixes with exponent approaching \(\varphi^2\). That result concerns guaranteed high-exponent suffixes and does not count the positions at which no cube ends.

The present result uses the exact regular language already established for cube-ending runs, but extracts its quantitative growth and combines it with the bounded zero-run theorem to obtain a sharp global order for the exceptional positions.

## Limitations
The theorem determines the correct order of \(Z(N)\) and an exact formula for run starts, but not an exact formula or leading asymptotic constant for \(Z(N)\) itself.

The argument is specific to the Fibonacci word and its Zeckendorf run language. No corresponding statement is asserted for arbitrary Sturmian words.

The source's run characterization is used as a theorem; it is not reproved from the Fibonacci morphism here.

## References
1. N. Rampersad, “Prefixes of the Fibonacci word that end with a cube,” arXiv:2111.09253v1, first public 2021-11-17; Comptes Rendus Mathématique 361 (2023), 323–330, DOI 10.5802/crmath.408.
2. J. Shallit, “Prefixes of the Fibonacci word,” arXiv:2302.04640, first public 2023-02-09; Theoretical Computer Science.
