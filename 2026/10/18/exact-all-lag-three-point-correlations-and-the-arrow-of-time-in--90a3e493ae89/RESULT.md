# Exact all-lag three-point correlations and the arrow of time in regular paperfolding dynamics

## Finding

The stationary regular-paperfolding sign process has an explicit three-site law at **every** triple of distinct integer times. In particular, the first time-oriented moment—the cubic correlation—is completely controlled by two dyadic valuation scales and the residue modulo four of an odd separation.

For any distinct \(t_0,t_1,t_2\in\mathbb Z\), let
\[
 m=\min_{0\le i<j\le 2}\nu_2(t_i-t_j).
\]
There is a unique pair of indices \(i,j\) with \(\nu_2(t_j-t_i)>m\); call this the *close pair*, and let \(k\) be the remaining index. Put
\[
 r=\nu_2(t_j-t_i)-m\ge1,\qquad
 d=(t_k-t_i)/2^m\in2\mathbb Z+1,
\]
and set \(\chi_4(d)=1\) if \(d\equiv1\pmod4\), and \(-1\) if \(d\equiv3\pmod4\). Then
\[
 \boxed{\mathbb E[S_{t_0}S_{t_1}S_{t_2}]
  =2^{-m}\chi_4(d)\begin{cases}
   0,&r=1,\\
   1/4,&r=2,\\
   -3/2^r,&r\ge3.
  \end{cases}}
\]
Changing the order of the close pair leaves this expression unchanged (the only potentially changed residue is immaterial when \(r=1\)).

The one-site moment is zero, and the pair correlation for every \(h\ne0\) is
\[
 C(h)=\mathbb E[S_0S_h]=\begin{cases}
 0,&\nu_2(h)=0,\\
 1-3/2^{\nu_2(h)},&\nu_2(h)\ge1.
 \end{cases}
\]
Consequently the **complete eight-probability law** at every triple is
\[
 \Pr(S_{t_i}=\varepsilon_i\text{ for }i=0,1,2)
 =\frac18\left(1+\sum_{0\le i<j\le2}C(t_j-t_i)\varepsilon_i\varepsilon_j
 +T(t_0,t_1,t_2)\varepsilon_0\varepsilon_1\varepsilon_2\right),
\]
where \(\varepsilon_i\in\{-1,1\}\) and \(T\) is the boxed cubic correlation.

For every \(0<a<b\), reflection of the time pattern reverses the cubic moment:
\[
 T(0,a,b)=-T(0,b-a,b).
\]
The two-point moments are reflection-symmetric. The oriented laws can nonetheless differ: the cylinder \((+1,+1,+1)\) has probability \(3/16\) at times \((0,1,4)\), but \(1/8\) at times \((0,3,4)\). Thus this stationary subshift is not time-reversible, and its complete pair correlation does not determine its three-point law.

## Assumptions and scope

Define the mod-four odd-unit character \(\chi_4\) as above. On the 2-adic integers \(\mathbb Z_2\) equipped with Haar probability, set \(f(x)=\chi_4(2^{-\nu_2(x)}x)\) for \(x\ne0\), giving \(f(0)\) any value. For Haar-uniform \(X\), let \(S_t=f(X+t)\), for all \(t\in\mathbb Z\). The orbit from the ordinary regular-paperfolding fixed point \(s_n=\chi_4(\operatorname{odd}(n+1))\), \(n\ge0\), has these finite-pattern frequencies. The integer triple has no magnitude or sign restriction other than distinctness. The theorem concerns this one fixed paperfolding dynamical measure, not arbitrary generalized paperfolding words or four-site laws.

For completeness, \(\nu_2(n)\) is the highest power-of-two exponent dividing nonzero integer \(n\), and \(\operatorname{odd}(n)=n/2^{\nu_2(n)}\). Haar-null exceptional integers in the 2-adic definition do not alter moments.

## Proof

**From the paperfolding word to Haar dynamics.** On each set of elements with valuation \(j\), the function \(f\) is determined by the residue modulo \(2^{j+2}\). Outside the cylinder \(2^K\mathbb Z_2\), the function is locally constant at a bounded modulus. Such cylinders have Haar mass \(2^{-K}\), so cylinder approximation proves that all finite products \(f(x+t_1)\cdots f(x+t_q)\) are Riemann-integrable on \(\mathbb Z_2\), with singularity sets of measure zero. Uniform distribution of the nonnegative integers modulo every power of two therefore identifies paperfolding orbit frequencies with Haar averages. The same argument identifies the stationary law and makes all the expectations below well-defined.

**One- and two-site moments.** Conditional on a fixed 2-adic valuation, the odd part is uniformly distributed between residues \(1\) and \(3\) modulo four, hence \(\mathbb E[f(X)]=0\). The auxiliary identity \(\mathbb E[(-1)^Xf(X+a)]=0\) holds for every integer \(a\), by translation and the fact that the odd residue class contributes zero. If \(h\) is odd, split the two-site integral by parity; the auxiliary identity implies \(C(h)=0\). If \(h\) is even, the odd \(X\)-part gives the constant \((-1)^{h/2}\), while the even \(X\)-part rescales to \(C(h/2)\), giving
\[
 C(h)=\tfrac12(-1)^{h/2}+\tfrac12C(h/2).
\]
Starting with odd \(h\) and inducting on \(\nu_2(h)\) yields the displayed pair-correlation formula.

**Reduction to the minimum separation scale.** Translate the time triple and write its three offsets as multiples of \(2^m\). If \(\nu_2(X)=j<m\), each observed sign equals the same odd-unit character \(\chi_4(2^{-j}X)\) multiplied by a constant depending on the offset. Since there are three factors, their product is an odd power of this character and its conditional expectation is zero. The complementary event \(X\in2^m\mathbb Z_2\) has probability \(2^{-m}\) and, after rescaling, gives an independent Haar variable. The full triple moment is therefore \(2^{-m}\) times the moment for offsets \((0,d,h)\), where \(d\) is odd, \(h\) is even, and \(\nu_2(h)=r\ge1\). The pair with even difference is unique because in any triple the minimum 2-adic distance valuation occurs twice.

**A signed pair integral.** Define \(R(q)=\mathbb E[(-1)^Yf(Y)f(Y+q)]\). For odd \(q\), splitting by parity and using \(\mathbb E[(-1)^Yf(Y+a)]=0\) yields \(R(q)=0\). For even \(q\), split by parity once more: odd \(Y\) contributes \(-(-1)^{q/2}/2\), and even \(Y\) contributes \(C(q/2)/2\). Thus
\[
 R(q)=\tfrac12\big(C(q/2)-(-1)^{q/2}\big)\qquad(q\text{ even}).
\]
Next split \(T(0,d,h)=\mathbb E[f(X)f(X+d)f(X+h)]\) by parity. If \(X\) is odd, then \(f(X)f(X+h)=(-1)^{h/2}\) and the remaining shifted sign has mean zero. If \(X=2Y\), then \(f(X+d)=\chi_4(d)(-1)^Y\), so
\[
 T(0,d,h)=\tfrac12\chi_4(d)R(h/2).
\]
When \(r=1\), \(h/2\) is odd and this vanishes. When \(r=2\), \(C(h/4)=0\) and \((-1)^{h/4}=-1\), giving \(\chi_4(d)/4\). When \(r\ge3\), \(C(h/4)=1-3/2^{r-2}\) and \((-1)^{h/4}=1\), giving \(-3\chi_4(d)/2^r\). Restoring the factor \(2^{-m}\) proves the theorem for all times.

**Joint words and reversal.** Expand \(\prod_{i=0}^2(1+\varepsilon_i S_{t_i})/8\) and use the moments above to obtain the eight-probability formula. For Haar-a.e. \(x\), \(f(-x)=-f(x)\), since \(\chi_4(-u)=-\chi_4(u)\) for odd \(u\). Reflecting all three times and changing \(X\) to \(-X\), then using stationarity, changes the sign of the triple expectation but not of any pair expectation. The two explicitly evaluated cylinders follow from \(C(1)=C(3)=0\), \(C(4)=1/4\), \(T(0,1,4)=1/4\), and \(T(0,3,4)=-1/4\). Their inequality demonstrates failure of time reversibility.

## Verification

Run `python3 verify.py` with Python's standard library. The verifier evaluates the exact predictor on every triple \((0,a,b)\) with \(-19\le a<b\le19\), \(a,b\ne0\), and on all nonzero two-site lags \(-32\le h\le32\). It independently averages the corresponding signs over all \(2^{13}\) residues modulo \(2^{13}\). If an evaluation reaches the zero residue, its value is replaced by zero. At most three residues per triple and two per pair have undefined 2-adic signs at this precision. The comparison therefore has the rigorous absolute error bounds \(3/2^{13}\) and \(2/2^{13}\), respectively. The program tests the two contrasting \((+1,+1,+1)\) cylinders exactly and reports 767 comparisons. This finite verification is not used as a substitute for the infinite proof above.

## Relationship to prior work

Van Enter and de Groote's paper on paperfolding overlap distributions studies the same underlying paperfolding construction and a two-replica overlap invariant; it does not state the above all-time, one-trajectory three-site moment or its reversal classification. Madill and Rampersad establish the odd-part representation and work out the abelian complexity of the regular paperfolding word, rather than these temporal correlations. Deng and Moody provide general two- and three-point correlation theory for model sets; the positive rigidity result for real internal spaces is not an evaluated formula for this 2-adic observable. The contribution here is the all-integer-lag valuation formula, full three-site law, and a quantitative orientation asymmetry. These comparisons do not establish exhaustive publication priority.

## Limitations

The theorem is for the regular paperfolding sign word, not every generalized paperfolding instruction sequence. It applies to three *distinct* integer times; repeated-time moments reduce to lower-order moments. It does not determine four-point laws or correlations of nonlinear observables. Prior general model-set machinery may implicitly facilitate the calculation, so a historical-priority risk remains. The verification code checks finite residues, whereas completeness for all integer lags is supplied by the Haar argument.

## References

1. A. C. D. van Enter and J. de Groote, *An Ultrametric State Space with a Dense Discrete Overlap Distribution: Paperfolding Sequences*, Journal of Statistical Physics (first public online 2010-12-21), DOI: `10.1007/s10955-010-0107-5`.
2. B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856 (first version 2012-08-14).
3. X. Deng and R. V. Moody, *How model sets can be determined by their two-point and three-point correlations*, arXiv:0901.4381 (2009).
