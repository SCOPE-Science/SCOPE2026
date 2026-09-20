# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The main theorem is built on Corollary 2.2 of Gheorghiciuc--Ward (2007), whose uniform-source error bound is explicitly stated to hold without requiring a fixed relationship between the number of windows and the substring length. Replacing their window-count parameter by \(N_k=n-k+1\) therefore gives
\[
\mathbb E D_{n,k}
=
d^k-d^k(1-d^{-k})^{N_k}
+
O_d(N_k^{-\varepsilon}\mu^k),
\]
with \(0<\mu<1\). Summing the errors over all \(k\) is \(O_d(1)\).

The reduction from the resulting occupancy deficit
\[
H(N,Q)=N-Q+Q(1-Q^{-1})^N
\]
to \(n f(Q/n)\), \(f(x)=1-x(1-e^{-1/x})\), was checked in two pieces. First, the exact increment
\[
H(N+1,Q)-H(N,Q)=1-(1-Q^{-1})^N
\]
bounds the cost of replacing \(N_k\) by \(n\); summing \((k-1)\min(1,n/d^k)\) gives \(O_d((\log n)^2)\). Second, the standard inequality for \(\log(1-z)\) bounds the binomial-to-exponential replacement by a summable geometric-grid series \(O_d(1)\).

The phase series is absolutely convergent because \(f(x)-1=-x+o(x)\) at zero and \(f(x)=1/(2x)+O(x^{-2})\) at infinity. The Mellin transform
\[
\mathcal M f(s)=\Gamma(1-s)/(s(1+s))
\]
was derived directly and independently checked numerically. Residues at \(2\pi i\ell/\log d\) give the Fourier coefficients in the record. A standalone artifact compares the defining phase series with the Fourier series over 1000 phases for each of \(d=2,3,4,10\), with maximum discrepancies at floating-point precision.

The elementary finite sandwich was checked separately. The delicate overlap fact is exact: two distinct uniform length-\(k\) windows agree with probability \(d^{-k}\), even if they overlap, because an overlap shift \(s<k\) imposes period \(s\) on \(k+s\) letters and leaves exactly \(s\) free symbols. Exhaustive enumeration confirms the sandwich for all binary words through length 16 and all ternary words through length 10.

## Originality

The originality claim is deliberately narrow.

Gheorghiciuc and Ward (2007) are strong prior art: they give a uniform approximation for the expected \(k\)-th subword complexity, and note an earlier uniform-source special case by Jacquet, Lučić and Szpankowski (2001). Ahmadi and Ward (2020) further analyze the \(k=\Theta(\log n)\) profile. These results make an all-length Mellin summation a natural possibility.

Flaxman, Harrow and Sorkin (2004) exactly determine the extremal distinct-substring count and state that a uniform random word is asymptotically optimal, localizing the potentially nonoptimal lengths between about \(\log_d n\) and \(2\log_d n\). A 2016 MathOverflow comment by Anthony Quas already gives the heuristic
\[
\binom n2-\frac{n\log n}{\log d},
\]
so the coefficient-one logarithmic term is not claimed as a previously unsuspected phenomenon.

Godbole (2026) studies the all-length expectation directly, but its proved lower bounds start the binary summation at \(3\log_2 n\) and the uniform \(d\ge3\) summation at \(2\log_d n\); no linear digital correction is stated.

Searches targeted the explicit periodic function, the Fourier coefficients involving \(\Gamma(1-\chi)/[\log d\,\chi(1+\chi)]\), all-length subword-complexity asymptotics, trie/suffix-tree profiles, and equivalent occupancy formulations. No inspected source stated
\[
R_{n,d}=n\log_d n+n\mathcal P_d(\{\log_d n\})+O((\log n)^2)
\]
or the explicit \(\mathcal P_d\) given here.

The principal residual risk is substantial but specific: older trie and suffix-tree profile analyses, especially Jacquet--Lučić--Szpankowski and related analytic-combinatorics work, may contain an equivalent periodic expansion under a different path-length/profile statistic. The result is therefore claimed only to the best of our knowledge, and specifically as the all-length distinct-substring formulation and explicit phase extraction.

## Value

The result resolves the entire linear-order correction to the random all-length distinct-substring count, rather than only its \(n\log n\) scale. It explains the correction as a classical digital oscillation, gives exact Fourier coefficients and phase mean, and shows that the binary oscillation is extraordinarily small. The finite collision sandwich is also a simple standalone route to a rigorous coefficient-one leading deficit and an additive \(O(n)\) comparison with the exact extremal count.

The result is more than a parameter tweak of the fixed-\(k\) literature: it requires a uniform all-level summation and isolates the global phase surviving at order \(n\).

## Limitations

The theorem is for fixed \(d\) and uniform i.i.d. letters. The \(O((\log n)^2)\) remainder relies on the 2007 uniform fixed-level approximation; the elementary proof alone gives only \(O(n)\). The next logarithmic-order phase term is not identified. No extension to nonuniform memoryless sources, variance, concentration, or dependent sources is claimed. Equivalent prior coverage through older trie/suffix-tree profile theorems remains a material originality risk. No independent validation is claimed.
