# Universal layer-order rule for two-flux atmospheric reflectance

## Finding
For any finite number of passive, symmetric, reciprocal two-flux layers with strictly positive diffuse reflectance and transmittance, the top-of-atmosphere diffuse reflectance is maximized, **simultaneously for every substrate reflectance**, by putting the largest semi-infinite-layer albedo at the top and sorting the remaining layers in decreasing semi-infinite albedo. The reverse order minimizes reflectance. The exact optimal orders are characterized by ties in a single intrinsic layer index; no layer-thickness-dependent comparison is needed.

More precisely, layer \(i\) has diffuse reflectance \(0<r_i<1\), transmittance \(0<t_i\), and passivity \(r_i+t_i\le1\). Put
\[
 w_i=\frac{1+r_i^2-t_i^2}{r_i}\ge2,
 \qquad p_i=\frac{w_i-\sqrt{w_i^2-4}}2\in(0,1].
\]
For every backing albedo \(\rho\in[0,1]\), any permutation with \(w_{\pi(1)}\le\cdots\le w_{\pi(n)}\) maximizes reflectance, and any permutation in reverse order minimizes it. The maximum (respectively minimum) is attained **only** by these sorted orders, except that layers with equal indices may be permuted freely. The order \(\pi(1),\ldots,\pi(n)\) is from the illuminated surface to the backing. The same sorting criterion is decreasing \(p_i\).

For a positive-thickness Kubelka–Munk sheet with scattering coefficient \(S_i>0\), absorption coefficient \(K_i\ge0\), and common diffuse-flux convention, the exact identity is
\[
 w_i=2\left(1+\frac{K_i}{S_i}\right).
\]
Thus, in the homogeneous two-flux atmosphere approximation, **ascending absorption-to-scattering ratio from top to bottom uniquely maximizes upward reflected diffuse flux**, modulo equal ratios; descending ratio minimizes it. This law holds for arbitrarily unequal positive thicknesses and all backing albedos in \([0,1]\).

## Assumptions and scope
The model is monochromatic, plane-parallel, time independent, without internal thermal emission or fluorescence. Each layer is *reciprocal and symmetric*: its diffuse reflectance is \(r_i\) and diffuse transmittance is \(t_i\) when illuminated from either side. There are no refractive-index mismatches at interfaces and no explicit angular modes beyond two opposing hemispheric fluxes. Passivity excludes a net energy source; strictly positive transmission excludes opaque or zero-thickness degeneracies. Only the order of a fixed multiset of layers changes, not its thicknesses, optical coefficients, or constituent count. Every claim holds for integer \(n\ge1\), arbitrary \(\rho\in[0,1]\), and the stated real parameter ranges; it does **not** assert ordering of wavelength-integrated broadband reflectance when \(K_i/S_i\) ranks cross between wavelengths.

Each layer acts on the albedo \(x\) below it via the standard adding formula
\[
 f_i(x)=r_i+\frac{t_i^2x}{1-r_ix},\qquad x\in[0,1].
\]
Consequently the stack reflectance is \(F_\pi(\rho)=f_{\pi(1)}\circ\cdots\circ f_{\pi(n)}(\rho)\). The semi-infinite albedo \(p_i\) is the smaller positive fixed point of \(f_i\), and is \(1\) when \(r_i+t_i=1\).

## Proof
**1. The layer maps are strictly increasing and passive.** For \(0\le x\le1\),
\[
 f_i'(x)=\frac{t_i^2}{(1-r_ix)^2}>0,
 \qquad 0< f_i(x)\le f_i(1)=r_i+\frac{t_i^2}{1-r_i}\le1.
\]
The last inequality follows from \(t_i\le1-r_i\). Thus every internal reflected-flux ratio stays in \([0,1]\).

**2. The exact swap-sign identity.** Introduce
\[
 M_i=\begin{pmatrix}t_i^2-r_i^2&r_i\\-r_i&1\end{pmatrix},
 \qquad f_i(x)=\frac{(M_i(x,1)^\mathsf T)_1}{(M_i(x,1)^\mathsf T)_2}.
\]
Direct multiplication, using the definition of \(w_i\), yields
\[
 M_iM_j-M_jM_i=r_ir_j(w_j-w_i)
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Let \(M_jM_i(x,1)^\mathsf T=(c,d)^\mathsf T\), and write \(h=r_ir_j(w_j-w_i)\). The two ratios then differ exactly by
\[
 f_i(f_j(x))-f_j(f_i(x))
 =\frac{h(d-cx)}{d(d+hx)}.
\]
Both denominators are positive for every \(x\in[0,1]\); also \(c/d=f_j(f_i(x))\in[0,1]\), so \(d-cx=d[1-xf_j(f_i(x))]\ge0\). If \(h\ne0\), strict positivity holds: \(xf_j(f_i(x))<1\) whenever \(x<1\); when \(x=1\), the only way the product could equal one is for **both** sheets to be lossless, which would force \(w_i=w_j=2\) and hence \(h=0\). Therefore
\[
 \operatorname{sgn}(f_i(f_j(x))-f_j(f_i(x)))=\operatorname{sgn}(w_j-w_i),
\]
strictly whenever \(w_i\ne w_j\), uniformly over the backing \(x\in[0,1]\). When the indices tie, the two maps commute exactly.

**3. Optimality and equality.** Consider any adjacent inverted pair \(w_i>w_j\) in a stack. Its lower suffix supplies some \(x\in[0,1]\). By step 2, interchanging the pair to put \(j\) first strictly increases reflectance. Applying the upper prefix, a composition of strictly increasing functions, preserves that strict inequality. Repeated adjacent swaps produce the nondecreasing-\(w\) order and prove its global optimality. If an alleged maximum contains an inversion it is strictly improvable. Equal-index adjacent layers commute, so every sorted permutation has the same value. Reversing all inequalities proves the corresponding minimum. This establishes all maximizing and minimizing permutations, including boundary albedos \(0,1\).

**4. Semi-infinite albedo.** Rearranging \(f_i(p)=p\) gives
\[
 p^2-w_ip+1=0.
\]
Passivity yields \(w_i\ge2\). The physically relevant smaller root is \(p_i=(w_i-\sqrt{w_i^2-4})/2\le1\), strictly decreasing with \(w_i\) on \((2,\infty)\). It approaches \(1\) at \(w_i=2\). The comparison is therefore equivalently decreasing semi-infinite albedo.

**5. Homogeneous Kubelka–Munk specialization.** Put \(a_i=1+K_i/S_i\), \(b_i=\sqrt{a_i^2-1}\), and \(\theta_i=S_ib_iL_i\) for thickness \(L_i>0\). The known exact finite-layer solution for \(b_i>0\) is
\[
 r_i=\frac{\sinh\theta_i}{a_i\sinh\theta_i+b_i\cosh\theta_i},
 \qquad t_i=\frac{b_i}{a_i\sinh\theta_i+b_i\cosh\theta_i}.
\]
Substitution, using \(\cosh^2\theta_i-\sinh^2\theta_i=1\), gives \((1+r_i^2-t_i^2)/r_i=2a_i\). When \(K_i=0\), the continuous limit is \(r_i=S_iL_i/(1+S_iL_i)\), \(t_i=1/(1+S_iL_i)\), so the same identity \(w_i=2\) holds. The sorting criterion is therefore exactly ascending \(K_i/S_i\), and the thickness cancels from every pairwise comparison.

## Verification
The dependency-free `verify.py` checks the exact rational matrix commutator and pairwise ordering sign in 4,800 instances including black and perfectly white backings; it compares all permutations for 96 sampled passive stacks of sizes two through five at three backing reflectances (10,944 exact comparisons), tests the conservative commuting case, and reproduces a three-layer exact example. These finite computations cross-check the algebra only; the universal theorem follows from the proof above.

For an explicit three-layer stack, take \((r_A,t_A)=(1/5,7/10)\), \((r_B,t_B)=(2/5,2/5)\), \((r_C,t_C)=(1/4,1/2)\), and backing \(\rho=1/5\). Their intrinsic indices are \(w_A=11/4\), \(w_B=5/2\), and \(w_C=13/4\). The unique maximum is the top-to-bottom order \(B,A,C\), with exact reflectance \(204/437\); the unique minimum is \(C,A,B\), with reflectance \(159/428\). Sorting by raw single-layer reflectance would instead put \(B,C,A\), which is not optimal. These three sheets are illustrative passive reciprocal two-flux layers, not asserted to arise from a common set of particular atmospheric constituents.

## Relationship to prior work
Kubelka and Munk (1931) introduced the homogeneous two-flux theory. Kubelka (1954), especially its multilayer adding law, equations (10), (18), and (19), already contains the necessary reflection/transmission composition formula. Moreover its equation (26) **explicitly uses the same intrinsic index** in a three-sheet *transmittance* comparison, proving that the index itself and some order effects are prior art. None of those statements explicitly gives the present global arbitrary-layer **reflectance maximization and minimization with all backing reflectivities and complete equality cases**. Hébert, Hersch, and Becker (2007) develop a more general multilayer compositional matrix framework, without asserting this specialized global optimization in the inspected complete article. Plass, Kattawar, and Catchings (1973) provide radiative transfer matrix composition for atmospheric layers. The proof here is a short specialization of classical adding formulas and makes no claim to a new physical transport equation or new matrix-composition principle.

## Limitations
Historical priority is not independently established: the sorting result may be implicit in older optical-coating guidance or a broader layer-composition rearrangement theorem. The 2015 two-flux survey of Hébert and Emmel was available only in abstract form for this comparison. The theorem does not extend without additional argument to differing refractive indices, directional solar beams, nonreciprocal/asymmetric layers, spectral rank crossing, refractive interfaces, thermal emission, or full angular multiple-scattering radiative transfer. Maximizing ideal modeled reflectance does not alone imply an engineering optimum for a real atmosphere or material.

## References
1. P. Kubelka and F. Munk, *Ein Beitrag zur Optik der Farbanstriche*, Zeitschrift für Technische Physik 12 (1931), 593–601.
2. P. Kubelka, *New Contributions to the Optics of Intensely Light-Scattering Materials. Part II: Nonhomogeneous Layers*, J. Opt. Soc. Am. 44 (1954), 330–335, https://doi.org/10.1364/JOSA.44.000330 (published April 1, 1954).
3. G. N. Plass, G. W. Kattawar, and F. E. Catchings, *Matrix operator theory of radiative transfer. 1: Rayleigh scattering*, Applied Optics 12 (1973), 314–329, https://doi.org/10.1364/AO.12.000314.
4. M. Hébert, R. D. Hersch, and J.-M. Becker, *Compositional reflectance and transmittance model for multilayer specimens*, J. Opt. Soc. Am. A 24 (2007), 2628–2644, https://doi.org/10.1364/JOSAA.24.002628.
5. M. Hébert and P. Emmel, *Two-Flux and Multiflux Matrix Models for Colored Surfaces*, Handbook of Advanced Computational Color Imaging (2015), https://doi.org/10.1007/978-3-319-07652-1_22-1 (abstract-only comparison).
