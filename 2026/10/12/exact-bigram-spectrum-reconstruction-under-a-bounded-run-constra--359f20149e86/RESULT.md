# Exact bigram-spectrum reconstruction under a bounded-run constraint

## Finding
Fix integers \(h\geq1\) and \(n\geq1\). Among length-\(n\) binary strings whose constant-symbol runs have length at most \(h\), let \(M_h(n)\) be the number of distinct multisets of all consecutive length-two substrings. Equivalently, \(M_h(n)\) is the maximum number of such strings in a code exactly reconstructible from its complete, multiplicity-preserving bigram spectrum. Set \(A_r(z)=1+z+\cdots+z^{(h-1)r}\) for every integer \(r\geq0\). Then
\[
\begin{aligned}
F_h(z):=\sum_{n\geq1}M_h(n)z^n
&=\sum_{m\geq0}z^{2m+1}\bigl(2A_{m+1}(z)A_m(z)-A_m(z)^2\bigr)\\
&\quad+2\sum_{m\geq0}z^{2m+2}A_{m+1}(z)^2\\
&=\frac{1}{(1-z)^2}\left(\frac{z+2z^2}{1-z^2}-\frac{2z^{h+1}(1+2z)}{1-z^{h+1}}+\frac{-z^3+2z^{h+2}+2z^{2h+2}}{1-z^{2h}}\right).
\end{aligned}
\]
For every fixed \(h\geq2\),
\[
M_h(n)=\frac{3(h-1)^2}{4h(h+1)}n^2+O_h(n),
\]
so the leading profile capacity relative to the unrestricted binary bigram channel is exactly \((h-1)^2/[h(h+1)]\). For \(h=1\), \(M_1(n)=1\) for odd \(n\) and \(M_1(n)=2\) for even \(n\).

For the first nontrivial run cap \(h=2\), the exact period-twelve quadratic quasipolynomial is
\[
M_2(n)=\frac{3n^2+20n+c_{n\bmod12}}{24},\qquad
(c_0,\ldots,c_{11})=(48,1,44,33,16,17,60,1,32,33,28,17).
\]
Let \(U_2(n)\) denote the number of individual admissible strings whose bigram multiset has exactly one admissible preimage. Then \(U_2(1)=0\), \(U_2(2)=4\), and for all integers \(n\geq3\),
\[
\begin{aligned}
U_2(n)={}&2\mathbf 1_{2\mid n}+4\mathbf 1_{3\mid n}+2\mathbf 1_{4\mid n}\\
&+2\mathbf 1_{n\equiv2\pmod3}+2\mathbf 1_{n\equiv2\pmod4}.
\end{aligned}
\]
Consequently at most eight admissible words are individually identifiable at each length, and **none** is individually identifiable whenever \(n\equiv1\pmod6\), although \(M_2(n)\) grows quadratically. Thus the uncoded and optimally coded reconstruction behaviors differ even with perfect full bigram coverage.

## Assumptions and scope
The alphabet is \(\{0,1\}\). A run is a maximal consecutive block of equal symbols; every run has length in \(\{1,\ldots,h\}\). The noiseless output is the complete multiset of length-two **overlapping** substrings, with multiplicities, in linear rather than cyclic words. Write the profile as \(p(w)=(a,u,v,b)\), where the coordinates count occurrences of \(00,01,10,11\), in that order. They sum to \(n-1\). For length one the profile is \((0,0,0,0)\), shared by both words. Distinct profiles are equivalent to perfect distinguishability; the theorem makes no claim about noisy or incomplete spectra.

Define the bounded-composition count, for integers \(r,k\geq0\), by
\[
B_h(r,k)=[t^k](1+t+\cdots+t^{h-1})^r,
\]
where \(B_h(0,0)=1\) and out-of-range coefficients vanish. For \(p=(a,u,v,b)\), set \(m=\min(u,v)\). The **exact number of admissible words with that profile** is
\[
N_h(p)=\begin{cases}
B_h(m+1,a)B_h(m,b)+B_h(m,a)B_h(m+1,b),&u=v,\\
B_h(m+1,a)B_h(m+1,b),&|u-v|=1,\\
0,&|u-v|>1.
\end{cases}
\]
This formula applies to all integer nonnegative profile coordinates; for each fixed length use only profiles summing to \(n-1\). In particular \(B_h(r,k)>0\) exactly when \(0\leq k\leq(h-1)r\), including \(r=0\).

## Proof
**Run-profile correspondence.** In a nonempty binary word, the run symbols alternate. Every \(01\) transition marks a zero-to-one run boundary, and every \(10\) transition marks a one-to-zero boundary. Consequently \(|u-v|\leq1\). When \(u=v=m\), the word either begins and ends with \(0\), in which case it has \(m+1\) zero-runs and \(m\) one-runs, or begins and ends with \(1\), reversing the numbers. When \(u=v+1\), the word begins with \(0\) and ends with \(1\), and each symbol has \(m+1\) runs; the case \(v=u+1\) reverses the symbols. Each zero-run of length \(\ell\) contributes \(\ell-1\) copies of \(00\), and similarly each one-run contributes \(\ell-1\) copies of \(11\). Assigning these nonnegative extras, each at most \(h-1\), to the prescribed runs is bijective with words having that profile. The bounded-composition product counts exactly the choices, proving \(N_h(p)\) without a finite-size assumption.

**Feasible-profile generating function.** For \(u=v=m\), possible internal-loop pairs \((a,b)\) are the union of two axis-aligned integer rectangles of side-index ranges \([0,(h-1)(m+1)]\times[0,(h-1)m]\) and its reversal; their intersection is the square with both upper indices \((h-1)m\). Weighting a pair by \(z^{a+b}\) gives \(2A_{m+1}A_m-A_m^2\), and the \(2m\) transitions contribute the factor \(z^{2m+1}\). For \(|u-v|=1\), there are two orientations, each with \(m+1\) runs of each symbol and \(2m+1\) transitions, giving \(2z^{2m+2}A_{m+1}^2\). These cases partition all attainable profiles, proving the first displayed generating function. Substituting \(A_r=(1-z^{(h-1)r+1})/(1-z)\), expanding and summing geometric series gives the displayed rational expression. This identity is valid formally for every integer \(h\geq1\), including \(h=1\).

**Asymptotics.** The rational function has at \(z=1\) a cubic pole whose leading coefficient is \(3(h-1)^2/[2h(h+1)]\), interpreted as zero at \(h=1\). All nontrivial roots of unity in its denominators contribute at most quadratic poles to the full function, and hence \(O_h(n)\) to its coefficients. Since \([z^n](1-z)^{-3}=n^2/2+O(n)\), the leading coefficient for \(M_h(n)\) follows. For the unrestricted channel, direct counting over \(|u-v|\leq1\) gives \(3n^2/4+O(n)\) attainable binary profiles; dividing the two leading constants proves the stated fraction.

**Exact period twelve for \(h=2\).** The denominator of the rational generating function divides \((1-z)^2(1-z^2)(1-z^3)(1-z^4)\). The given twelve residues satisfy the exact finite polynomial identity obtained by multiplying the proposed quasipolynomial generating series and the rational expression by \((1-z)^3(1-z^{12})\). The standalone verifier `verify_identity.py` checks this identity by exact integer polynomial arithmetic; the coefficient argument is valid for all \(n\), not merely the tested initial values.

**Individually unique spectra.** For \(h=2\), the bounded-composition numbers are binomial coefficients \(B_2(r,k)=\binom{r}{k}\). If \(|u-v|=1\), the fiber is a product \(\binom{m+1}{a}\binom{m+1}{b}\), equal to one precisely when each of \(a,b\) lies at an endpoint of \([0,m+1]\). The four cases have lengths \(2(m+1)\), two cases at \(3(m+1)\), and \(4(m+1)\); the two transition orientations double these counts. If \(u=v=m\geq1\), the sum of the two nonnegative binomial products can equal one only if one product is zero and the other one: exactly \(a=m+1\) and \(b\in\{0,m\}\), or the symbol-reversed alternatives. These have lengths \(3m+2\) and \(4m+2\), two cases each. When \(m=0\), the length-one profile is shared by \(0\) and \(1\), and the length-two constant words are uniquely recoverable. Gathering the preceding cases gives the stated formula for \(U_2(n)\); its residues show the zero class \(n\equiv1\pmod6\). This completes the proof.

**Encoding and sharpness.** Each profile fiber is an indistinguishability class, so a uniquely reconstructible code takes at most one word from each fiber, while selecting exactly one per nonempty fiber reaches \(M_h(n)\). A concrete representative is obtained by determining the transition orientations and numbers of alternating zero- and one-runs, choosing a feasible orientation, then distributing the \(a\) and \(b\) extra repeat symbols greedily among their respective runs with capacity \(h-1\) each. The resulting word has the prescribed profile, establishing attainability and explicit decoding by a profile-to-representative table or the stated construction.

## Verification
Execute `python3 verify_profile.py` and `python3 verify_identity.py` using standard-library Python. The former enumerates every binary word of lengths \(1\) through \(17\) for run caps \(1\) through \(5\), computes all profile fibers independently, verifies the exact bounded-composition fiber formula and reconstructs a representative per profile. It separately checks coefficient identities for run caps \(1\) through \(20\) and lengths through \(500\), and the unique-fiber count for \(h=2\). The latter proves the claimed period-twelve coefficient identity as equality of finite integer polynomials after clearing denominators; it is a finite algebraic certificate for an infinite coefficient statement. Neither test is substituted for the run decomposition and generating-function proof.

## Relationship to prior work
Kiah, Puleo and Milenkovic [1] introduced and analyzed DNA sequence-profile reconstruction and restricted de Bruijn-graph counts, including asymptotic profile enumerations under restrictions on allowed substring types. The present restriction is instead on **maximal run length in the underlying word**, and the result provides a closed rational series for **every** run cap, exact finite profile fibers, and a sharp code cardinality. Jacquet, Knessl and Szpankowski [2] derived general enumerations and asymptotics for unrestricted Markov types; the balanced/cyclic binary frequency-matrix example there does not contain the bounded-run constraint or the linear-word singleton census here. Gabrys and Milenkovic [3] study code reconstruction from longer substring multispectra, usually with read length growing with block length; their theorems do not settle the fixed two-symbol bounded-run enumeration. The classical Euler-trail correspondence and generating-function techniques used here are not claimed to be new individually.

## Limitations
The statements concern complete noiseless multiplicity-preserving bigram observations, binary words, and a fixed finite run cap. They do not claim unique recovery of every admissible word: indeed, in one infinite congruence class no word is individually recoverable under \(h=2\). A code of maximum size need not have good error correction, large rate, or efficient index encoding, and the polynomial-size profile alphabet precludes a positive asymptotic rate at fixed read length. No assertion of absolute publication priority follows from literature searches; unindexed run-constrained Markov-type treatments remain a bibliographic risk.

## References
[1] H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837v1 (first public 2014-10-31); expanded as *Codes for DNA Sequence Profiles*, arXiv:1410.8837v2 (2015-11-03). https://arxiv.org/abs/1410.8837

[2] P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, Analysis of Algorithms (2010), full open manuscript at https://www.cs.purdue.edu/homes/spa/papers/aofa10.pdf .

[3] R. Gabrys, O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (2018). https://arxiv.org/abs/1804.04548
