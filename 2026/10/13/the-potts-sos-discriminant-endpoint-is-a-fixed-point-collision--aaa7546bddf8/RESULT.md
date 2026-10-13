# The Potts–SOS discriminant endpoint is a fixed-point collision
## Finding
For the three-state Potts–SOS model on the Cayley tree of order \(k=2\), restrict the periodic boundary-law equations of Rasulova to the analyzed sector \(z_0=t_0=1\) and the coupling line \(r=\theta^2\). Define
\[
f_\theta(z)=\left(\frac{2+\theta z}{2\theta+z}\right)^2,
\qquad z>0,
\]
and let \(\theta_c\) be the unique positive root of
\[
P(\theta)=3\theta^4+10\theta^3+6\theta^2-1.
\]
Then \(\theta_c=0.3235915534880762133\ldots\), and this sector has a genuine nontranslation-invariant period-two orbit exactly for \(0<\theta<\theta_c\), not at \(\theta=\theta_c\). Its two values are
\[
z_\pm(\theta)=\frac{2\{-Q(\theta)\pm(1-\theta^2)\sqrt{-P(\theta)}\}}{\theta^2(\theta+2)^2},
\qquad Q(\theta)=\theta^4+5\theta^3+4\theta^2-1.
\]
At \(\theta=\theta_c\) these coalesce at
\[
z_c=-\frac{2Q(\theta_c)}{\theta_c^2(\theta_c+2)^2}=1.4177905789883524319\ldots,
\]
and \(f_{\theta_c}(z_c)=z_c\) with \(f'_{\theta_c}(z_c)=-1\). Thus the double root used in the source's \(D=0\) argument is translation invariant and does not furnish the claimed nontranslation-invariant endpoint measure in this sector. Moreover,
\[
z_+(\theta)-z_-(\theta)\sim
\frac{4(1-\theta_c^2)\sqrt{P'(\theta_c)}}{\theta_c^2(\theta_c+2)^2}
\sqrt{\theta_c-\theta},
\]
so the two-cycle collapses through a square-root flip bifurcation. This claim is only about the \(z_0=t_0=1\), \(r=\theta^2\) sector and does not rule out other periodic Gibbs measures from other branches of the full boundary-law system.

## Assumptions and scope
The spin space and nearest-neighbour Potts–SOS Hamiltonian are those of M. A. Rasulova, *Periodic Gibbs Measures for the Potts–SOS Model on a Cayley Tree*, Theoretical and Mathematical Physics 199 (2019), 586–592, DOI:10.1134/S0040577919040081. The calculation is restricted to Cayley-tree order \(k=2\), to the source's periodic subcase \(z_0=t_0=1\), and to the distinguished parameter line \(r=\theta^2\). Positive solutions \(z\) of \(f_\theta(f_\theta(z))=z\) that also satisfy \(f_\theta(z)=z\) are translation invariant and therefore must be excluded when counting nontranslation-invariant period-two boundary laws.

## Proof
On \(r=\theta^2\), the source map becomes
\[
f_\theta(z)=\left(\frac{2+\theta z}{2\theta+z}\right)^2.
\]
Direct exact reduction gives
\[
\operatorname{num}\bigl(f_\theta(f_\theta(z))-z\bigr)=N_\theta(z)H_\theta(z),
\]
where \(N_\theta(z)=\operatorname{num}(f_\theta(z)-z)\) and
\[
H_\theta(z)=\theta^2(\theta+2)^2z^2+4Q(\theta)z+4\theta^2(2\theta+1)^2,
\]
with \(Q(\theta)=\theta^4+5\theta^3+4\theta^2-1\). Thus every nonfixed period-two point must be a root of \(H_\theta\).

The discriminant and fixed-point resultant factor as
\[
\operatorname{{disc}}_z H_\theta=-16(\theta-1)^2(\theta+1)^2P(\theta),
\]
\[
\operatorname{{Res}}_z(N_\theta,H_\theta)=256(\theta-1)^6(\theta+1)^6P(\theta),
\]
where \(P(\theta)=3\theta^4+10\theta^3+6\theta^2-1\). Since
\[
P'(\theta)=6\theta(2\theta+1)(\theta+2)>0
\]
for \(\theta>0\), \(P\) has one positive zero \(\theta_c\). Also
\[
Q(\theta)=P(\theta)-\theta^2(\theta+2)(2\theta+1),
\]
so \(Q(\theta)<0\) for \(0<\theta\le\theta_c\). Hence, for \(0<\theta<\theta_c\), the quadratic \(H_\theta\) has two distinct positive roots and the resultant is nonzero, so neither root is fixed. They are therefore the two points of one genuine two-cycle, and the quadratic formula yields the displayed \(z_\pm(\theta)\).

At \(\theta=\theta_c\), \(H_\theta\) has the unique double root
\[
z_c=-\frac{2Q(\theta_c)}{\theta_c^2(\theta_c+2)^2}>0.
\]
Substitution gives the exact identity
\[
N_\theta(z_c)=
\frac{4(\theta-1)^2(\theta+1)^2P(\theta)
(\theta^6+8\theta^5+18\theta^4+6\theta^3-8\theta^2+2)}
{\theta^6(\theta+2)^6},
\]
where here \(z_c=-2Q(\theta)/(\theta^2(\theta+2)^2)\). Therefore \(N_{\theta_c}(z_c)=0\): the double root is a fixed point. A second exact reduction gives \(f'_{\theta_c}(z_c)=-1\), identifying the collision as a flip threshold.

For \(\theta_c<\theta<1\), the discriminant of \(H_\theta\) is negative. At \(\theta=1\), \(H_1(z)=9(z+2)^2\) has no positive root, and for \(\theta>1\) the discriminant is again negative. Thus this sector has no genuine positive two-cycle for \(\theta\ge\theta_c\). Finally, the explicit difference of the two roots is
\[
z_+(\theta)-z_-(\theta)=
\frac{4(1-\theta^2)\sqrt{-P(\theta)}}{\theta^2(\theta+2)^2},
\]
and Taylor expansion of \(P\) at its simple zero gives the stated square-root law.

## Verification
The bundled `verify.py` symbolically checks the factorization of \(f_\theta^2(z)-z\), the discriminant, the resultant, the endpoint fixed-point identity, and the derivative \(f'_{\theta_c}(z_c)=-1\). It also checks a rational parameter below threshold where the two positive roots are exchanged by \(f_\theta\), and a parameter above threshold where the discriminant is negative. The exact algebraic identities are the proof; numerical values are only diagnostics.

## Relationship to prior work
The 2019 paper derives the same one-dimensional map in this sector, factors away fixed points, and states for \(k=2\) that a quadratic with discriminant \(D\) supplies nontranslation-invariant periodic measures. On \(r=\theta^2\), it records
\[
D=-16\theta^8(\theta^2-1)^2P(\theta)
\]
and reports \(\theta_D\approx0.32359\). It then says that \(D=0\) and the relevant middle coefficient being negative imply at least one nontranslation-invariant periodic Gibbs measure at \(\theta=\theta_D\). The calculation above identifies the missing fixed-point check: at that endpoint, the repeated quadratic root is a fixed point and therefore translation invariant.

The earlier preprint arXiv:1803.00768 establishes periodic Gibbs-measure existence for the Potts–SOS model but does not, in the available abstract, state this endpoint correction. The 2021 paper arXiv:2104.00973 concerns extremality of translation-invariant Gibbs measures rather than this period-two endpoint. A 2022 article with the same Potts–SOS model title, DOI:10.29229/uzmj.2022-2-14, is a plausible comparison source; no exact endpoint formula or correction was found in searchable metadata, but a verified full text was not available for inspection. Exact-form and alias searches found no published statement of the fixed-point collision or the corrected strict endpoint in this sector.

## Limitations
The result is local to the source's \(z_0=t_0=1\) reduction and the line \(r=\theta^2\). It corrects the endpoint interpretation of that quadratic but does not prove that the full four-variable boundary-law system has no other nontranslation-invariant solution at \(\theta=\theta_c\). It also does not classify other coupling lines or other Cayley-tree orders. The 2022 same-model follow-up could not be inspected in full and remains a residual originality risk.

## References
1. M. M. Rahmatullaev and M. A. Rasulova, *Periodic Gibbs measures for the Potts-SOS model on a Cayley tree*, arXiv:1803.00768v1, first public 2018-03-02.
2. M. A. Rasulova, *On periodic Gibbs measures for Potts-SOS model on the Cayley tree*, arXiv:1805.04482v1, 2018-05-10.
3. M. A. Rasulova, *Periodic Gibbs Measures for the Potts–SOS Model on a Cayley Tree*, Theoretical and Mathematical Physics 199 (2019), 586–592, DOI:10.1134/S0040577919040081.
4. M. M. Rahmatullaev and M. A. Rasulova, *Extremality of translation-invariant Gibbs measures for the Potts–SOS model on the Cayley tree*, arXiv:2104.00973v1; Journal of Statistical Mechanics: Theory and Experiment (2021), DOI:10.1088/1742-5468/ac08ff.
5. M. A. Rasulova, *Periodic Gibbs measures for the three-state Potts-SOS model on a Cayley tree*, Uzbek Mathematical Journal 66(2) (2022), 150–155, DOI:10.29229/uzmj.2022-2-14.
