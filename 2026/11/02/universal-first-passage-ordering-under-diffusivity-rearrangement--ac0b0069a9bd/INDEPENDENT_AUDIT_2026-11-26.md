# Independent mathematical audit

## correctness

PASS

The optical map is bi-Lipschitz and yields generator ∂yy by the stated optical-pullback definition. Equimeasurability fixes Y and leaves only u=∫₀ᵃD⁻¹ᐟ² to vary. Layer cake bounds this prefix integral by the smallest and largest a-mass slices of the sorted optical density; monotone diffusivity realizes both. Sliding the length-a window from 0 to L−a in the sorted profile and cyclically shifting the full profile realizes every intermediate u by continuity. Pathwise, the upper-reflected unkilled coordinate is √2 B_t+min{u,Y−sup_{s≤t}√2 B_s}, increasing in u, so its first crossing of zero is ordered. The same ordered Brownian segment in each cycle and common reset intervals preserve completion order by induction. For u<v, pick t₀ with positive reset survival; a small Brownian tube around a descending path crossing −u but not −v by t₀ prevents upper reflection and has positive probability. On this event and no first reset before t₀ the laws separate. The same support argument gives positive success probability per cycle, hence almost-sure completion. The renewal recursion splits on the first reset; the Poisson transform and mean follow from qₛ''=s qₛ with qₛ(0)=1, qₛ'(Y)=0 and a geometric renewal calculation. For the illustrative two-material example, Y=.75 and the two starts are .2 and .4. The display uses u and ν for the same endpoint/window-integral quantities; the definitions disambiguate this notational slip.

## originality

PASS

The optical transform and Poisson mean are established prior components, as is propagation of one-cycle stochastic order through a shared renewal clock. The sort order here concerns static equimeasurable materials on a finite reflecting interval at a fixed physical start/reset point. The inspected results do not provide the sharp design-law classification, in particular the exact continuum of attainable laws. The supported distinct claim is that classification, not a new general renewal principle.

## value

PASS

For an inventory-constrained design, the result replaces optimizing any particular mean or resetting rate with one sharp pathwise order and shows exactly how many laws the material placement can realize: a single continuous interval of strictly ordered parameters, possibly degenerate for a constant inventory. This gives clock-independent choices for objectives such as deadline failure, quantiles and monotone penalties without solving the distribution for each profile. Sharp attainability and independence of the clock law give the design statement value beyond the known optical transform and Poisson mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
