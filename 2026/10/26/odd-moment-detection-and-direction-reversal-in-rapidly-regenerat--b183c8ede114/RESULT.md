# Odd-moment detection and direction reversal in rapidly regenerated random environments

## Finding
Let \(W\) be a random variable taking values in \((0,1)\), let \(\nu\) be its law, and suppose \(\mathbb E W=1/2\). For the nearest-neighbor walk on \(\mathbb Z\) in a spatially iid environment whose entire field is independently resampled with probability \(p\) after each step, write \(v(p)\) for its annealed almost-sure limiting velocity, \(p\in(0,1]\).

If \(\nu\) is invariant under \(w\mapsto1-w\), then \(v(p)=0\) for all \(p>0\). Otherwise there exists a least \(r\ge1\) with \(\mu_{2r+1}:=\mathbb E[(W-1/2)^{2r+1}]\ne0\). For an independent copy \(W'\),
\[
 v(p)=2\,\mu_{2r+1}\,\mathbb E[(W-W')^{2r}](1-p)^{4r}+O((1-p)^{4r+1})\qquad (p\uparrow1).
\]
The even-difference factor is strictly positive. Thus vanishing velocity throughout any open interval immediately below full refreshing is equivalent to reflection symmetry of the single-site environment distribution. Its nonzero high-refresh direction is dictated by the first nonzero odd centered moment, regardless of the static walk's direction.

In particular, if \(\mu_3\ne0\), then
\[
 v(p)=4\operatorname{Var}(W)\mu_3(1-p)^4+O((1-p)^5).
\]

## Assumptions and scope
At every site \(x\in\mathbb Z\), an iid sample \(W_x\sim\nu\) gives right-jump probability \(W_x\) and left-jump probability \(1-W_x\). Conditional on the currently fixed field, successive steps use these site probabilities. Independently after each step, with probability \(p\), the entire field is resampled independently, and otherwise it is retained. We study the limiting speed for \(p>0\) in the Martin–Nagel geometric-regeneration model. The comparison to a static walk uses \(p=0\) only for qualitative transience, not the velocity formula. No uniform ellipticity constant is needed for the principal expansion, though the explicit example is uniformly elliptic.

Denote by \(Z_m\) the position after \(m\) steps of the ordinary *static*, spatially iid random-environment walk, averaged over walk and sites, and let \(a_m=\mathbb EZ_m\). The published regenerative formula is
\[
 v(p)=p^2\sum_{m\ge1}a_m(1-p)^{m-1}.
\]
Since \(|a_m|\le m\), this series converges absolutely for \(0<p\le1\). The nonzero coefficient index \(r\) is always finite for a nonsymmetric law: if all odd centered moments vanish, the signed difference between the centered law and its reflection integrates every polynomial to zero, hence every continuous function by polynomial density on the compact interval \([-1/2,1/2]\), proving equality of the laws.

## Proof
Write \(\bar\nu=(\nu+\nu^\#)/2\), where \(\nu^\#\) is the image under \(w\mapsto1-w\). Reflection of every path shows \(\mathbb E_{\bar\nu}Z_m=0\) at every time \(m\). The measures \(\nu\) and \(\bar\nu\) have identical polynomial moments of degrees at most \(2r\): for centered monomials, even moments agree automatically, and odd moments below \(2r+1\) vanish by the choice of \(r\).

Fix a path of \(m\) nearest-neighbor steps, with \(R_x\) rightward and \(L_x\) leftward departures from each visited site \(x\). Its annealed probability is the finite product
\[
 \prod_x\mathbb E_\nu[W^{R_x}(1-W)^{L_x}].
\]
For any \(m\le4r\), no site can have more than \(2r\) departures: successive visits to one site require at least two steps between them, and a site other than the origin is first reached after at least one step. Consequently every path has exactly the same annealed probability under \(\nu\) as under \(\bar\nu\), so \(a_m=0\) for \(1\le m\le4r\).

At time \(4r+1\), the only possible departure count above \(2r\) is \(2r+1\) departures from the origin. The corresponding paths consist of precisely \(2r\) two-step excursions \(0\to\pm1\to0\), followed by a final step \(0\to\pm1\). All other paths have identical probability under \(\nu\) and \(\bar\nu\), and hence cancel in the difference of averaged terminal positions.

For an excursion sequence containing \(k\) right excursions and \(2r-k\) left excursions, set \(m_j=\mathbb EW^j\). Lower centered odd moments vanish, so \(\mathbb E(1-W)^j=m_j\) for every \(j\le2r\). Thus the product of the two neighboring-site return factors is \(m_km_{2r-k}\). The final step's expected *signed* contribution at the origin is
\[
 F_k(\nu)=\mathbb E_\nu[W^k(1-W)^{2r-k}(2W-1)].
\]
The polynomial in brackets has degree \(2r+1\), leading coefficient \(2(-1)^k\), while all its other coefficients involve lower moments that agree under \(\nu\) and \(\bar\nu\). Its expectation therefore changes by \(2(-1)^k\mu_{2r+1}\) upon replacing \(\bar\nu\) by \(\nu\). Summing the \(\binom{2r}{k}\) excursion arrangements gives
\[
 a_{4r+1}=2\mu_{2r+1}\sum_{k=0}^{2r}(-1)^k\binom{2r}{k}m_km_{2r-k}
 =2\mu_{2r+1}\mathbb E[(W-W')^{2r}].
\]
The equality on the right is the binomial expansion for independent \(W,W'\). It is positive apart from the sign of \(\mu_{2r+1}\), since \(\nu\) is not a point mass (point masses of mean \(1/2\) are symmetric). Inserting \(a_1=\cdots=a_{4r}=0\) into the published analytic speed series and expanding its prefactor \(p^2\) completes the claimed asymptotic. If \(\nu\) is symmetric, reflection directly gives zero speed for every \(p\).

**Opposite directions example.** Assign probabilities \((2/25,3/5,8/25)\) to the three sitewise right-jump probabilities \((1/20,2/5,4/5)\), respectively. Exact arithmetic gives \(\mathbb EW=1/2\), \(\operatorname{Var}(W)=51/1000\), \(\mu_3=3/4000\). Thus \(v(p)=153(1-p)^4/10^6+O((1-p)^5)>0\) for sufficiently large \(p<1\). Yet
\[
 \mathbb E\log\frac{1-W}{W}=\frac1{25}\log\frac{19^2\,3^{15}}{2^{31}}>0,
\]
so the static iid environment yields a walk transient to the *left* by the classical one-dimensional log-ratio criterion. This example is uniformly elliptic; its speed at full refresh is zero.

## Verification
The accompanying standard-library `verify.py` computes exact annealed path means by enumerating \(2^m\) step sequences, multiplying the sitewise mixed moments using rational arithmetic. It checks that the three-atom example has zero static-block mean through time four and the predicted \(a_5=153/10^6\). It also tests an unrelated, nonsymmetric four-atom law with \(\mu_3=0\ne\mu_5\), verifying zero means through time eight and the predicted \(a_9=554742/30517578125\). Finally, it checks a symmetric law to time seven. These are finite validation checks only; the proof of the theorem for every \(r\) is the departure-count argument above. Execute `python verify.py` (no external dependencies).

## Relationship to prior work
Martin and Nagel (2026) derive the regenerative speed series and general differentiability identities, including the mean-dependent second derivative at full refreshing. Their general identities enable expansion but do not state the first nonzero balanced-environment term or classify all reflection-symmetric environments. The exact order \(4r\), positive factor \(2\mathbb E(W-W')^{2r}\), and static-left/dynamic-right construction come from the path comparison here. The cooling-environment and exclusion-driven walk literature studies related regimes but with different environment-refresh mechanisms and without this complete balanced moment hierarchy.

## Limitations
The theorem concerns the specified independent *whole-field* Bernoulli refresh model in one spatial dimension and the asymptotic regime \(p\uparrow1\). It does not prove global monotonicity of \(v(p)\), a full sign classification away from full refreshing, or a static limiting velocity at \(p=0\). The finite exact checks cannot replace the general analytic proof. Priority under older alternative terminology has not been independently audited.

## References
- R. Martin and J. Nagel, *Random walk in a regenerating random environment*, arXiv:2610.11919v1 (first public October 8, 2026), especially the geometric-regeneration velocity series and differentiability results.
- *Random walks in cooling random environments*, arXiv:1610.00641 (2016), for related refreshing regimes and the standard static one-dimensional transience criterion.
- F. Huveneers and F. Simenhaus, *Random walk driven by the simple exclusion process*, arXiv:1404.4187 (2014), for a different interacting dynamic-environment directional comparison.
